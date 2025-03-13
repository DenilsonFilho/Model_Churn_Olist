import os
import sqlalchemy

TRAIN_DIR = os.path.dirname( os.path.abspath( __file__ ) )
DATA_PREP_DIR = os.path.dirname( TRAIN_DIR )
BASE_DIR = os.path.dirname( DATA_PREP_DIR )
DATA_DIR = os.path.join( os.path.dirname( os.path.dirname( os.path.dirname( BASE_DIR ))), 'data')

print(DATA_DIR)

