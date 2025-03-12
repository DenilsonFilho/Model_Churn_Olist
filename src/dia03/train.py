import pandas as pd
import sqlalchemy
import os
from sklearn import tree
from sklearn import metrics

EP_DIR = os.path.dirname( os.path.abspath( __file__ ) )
SRC_DIR = os.path.dirname( EP_DIR )
BASE_DIR = os.path.dirname( SRC_DIR )
DATA_DIR = os.path.join( BASE_DIR, 'data' )


def import_query(path, **kwards):
    with open( path, 'r', **kwards ) as file_open:
        result = file_open.read()
    return result

def connect_db():
    return sqlalchemy.create_engine( 'sqlite:///' + os.path.join( DATA_DIR, 'olist.db' ) )

query = import_query(os.path.join(EP_DIR, 'create_safra.sql'))
con = connect_db()

#inspector = sqlalchemy.inspect(con)
#print( inspector.get_table_names() )

df = pd.read_sql( query, con )
columns = df.columns.to_list()

to_remove = ['seller_id', 'seller_city']
target = 'flag_model'

for i in to_remove + [target]:
    columns.remove(i)
    
cat_features = df[columns].dtypes[ df[columns].dtypes == 'object' ].index.to_list()
num_features = list(set( df[columns] ) - set( cat_features ))

clf = tree.DecisionTreeClassifier(max_depth=10)
clf.fit( df[num_features], df[target] )

y_pred = clf.predict( df[num_features] )
x_prob = clf.predict_proba( df[num_features] )

metrics.confusion_matrix(df[target], y_pred)


features_importances = pd.Series(clf.feature_importances_, index=num_features)
print(features_importances.sort_values(ascending=False)[:20])