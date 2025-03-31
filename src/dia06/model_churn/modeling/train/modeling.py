import pandas as pd 
import os
import sqlalchemy
from sklearn import tree
from sklearn import model_selection
from sklearn import metrics
from sklearn import preprocessing

TRAIN_DIR = os.path.join( os.path.abspath('.'), 'src', 'dia05', 'model_churn', 'modeling', 'train')
TRAIN_DIR = os.path.dirname( os.path.abspath( __file__ ) )
MODELING_DIR = os.path.dirname( TRAIN_DIR )
BASE_DIR = os.path.dirname( MODELING_DIR )
DATA_DIR = os.path.join( os.path.dirname( os.path.dirname( os.path.dirname( BASE_DIR ))), 'data')

engine = sqlalchemy.create_engine( 'sqlite:///' + os.path.join( DATA_DIR, 'olist.db' ) )
conn = engine.connect()

abt = pd.read_sql_table('tb_abt_churn', conn)

df_oot = abt[ abt['dt_ref'] == abt['dt_ref'].max() ].copy() # Filtrando base out of time
df_abt = abt[ abt['dt_ref'] < abt['dt_ref'].max() ].copy() # Filtrando base ABT

target = 'flag_churn'
to_remove = ['dt_ref', 'seller_city', 'seller_id', target] 
features = df_abt.columns.tolist()
for f in to_remove:
    features.remove( f )
    
cat_features = df_abt[features].dtypes[ df_abt[features].dtypes == 'object' ].index.tolist()
num_features = list( set( features ) - set( cat_features ) )
    
X = df_abt[features]    
y = df_abt[target]

X_train, X_test, y_train, y_test = model_selection.train_test_split(X,
                                                                    y,
                                                                    test_size=0.2,
                                                                    random_state=1992)

X_train.reset_index(drop=True, inplace=True)
X_test.reset_index(drop=True, inplace=True)

onehot = preprocessing.OneHotEncoder(sparse_output=False, handle_unknown='ignore')
onehot.fit( X_train[cat_features] )

onehot_df = pd.DataFrame(onehot.transform( X_train[cat_features] ), 
             columns=onehot.get_feature_names_out(cat_features))

df_train = pd.concat([X_train[num_features], onehot_df], axis=1)
df_train= df_train.rename(str,axis="columns") 
features_fit = df_train.columns.tolist()

# Modelo
clf = tree.DecisionTreeClassifier(min_samples_leaf=100)
clf.fit( df_train[features_fit], y_train )

pd.Series(clf.feature_importances_, index=df_train.columns).sort_values(ascending=False)[:10]

# Analise na base de treino

y_train_pred = clf.predict(df_train)
print('Base Treino:', metrics.accuracy_score(y_train, y_train_pred))

# Analise na base de teste
onehot_df_test = pd.DataFrame(onehot.transform( X_test[cat_features] ), 
             columns=onehot.get_feature_names_out(cat_features))
df_predict = pd.concat([X_test[num_features], onehot_df_test], axis=1)
df_predict = df_predict.rename(str, axis='columns')
y_test_pred = clf.predict(df_predict)
print('Base test:', metrics.accuracy_score(y_test, y_test_pred))

# Analise na base de out of time
df_oot.reset_index(drop=True, inplace=True)
onehot_df_oot = pd.DataFrame(onehot.transform( df_oot[cat_features] ), 
             columns=onehot.get_feature_names_out(cat_features))
df_predict_oot = pd.concat([df_oot[num_features], onehot_df_oot], axis=1)
df_predict_oot = df_predict_oot.rename(str, axis='columns')
oot_pred = clf.predict(df_predict_oot)
print('Base out of time:', metrics.accuracy_score(df_oot[target], oot_pred))

# Fazendo o predict
df_abt_onehot = pd.DataFrame(onehot.transform( abt[cat_features] ), 
             columns=onehot.get_feature_names_out(cat_features))
df_abt_predict = pd.concat([abt[num_features], df_abt_onehot], axis=1)
df_abt_predict = df_abt_predict.rename(str, axis='columns')

probs = clf.predict_proba(df_abt_predict)

abt['score_churn'] = probs = clf.predict_proba(df_abt_predict)[:,1]