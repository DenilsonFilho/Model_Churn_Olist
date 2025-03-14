import pandas as pd
import sqlalchemy
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--date', '-d', help='Data de referência da safra. Formato YYYY-MM-DD', default='2017-04-01')

args = parser.parse_args()
date_ref = args.date

EP_DIR = os.path.dirname( os.path.abspath( __file__ ) )
SRC_DIR = os.path.dirname( EP_DIR )
BASE_DIR = os.path.dirname( SRC_DIR )
DATA_DIR = os.path.join( BASE_DIR, 'data' )


def import_query(path, **kwargs):
    with open( path, 'r', **kwargs ) as file_open:
        result = file_open.read()
        return result

def connect_db():
    return sqlalchemy.create_engine( 'sqlite:///' + os.path.join( DATA_DIR, 'olist.db' ) )

query = import_query(os.path.join(EP_DIR, 'query_2.sql'))
query = query.format(date=date_ref)

con = connect_db()
con = con.connect()

try:
    print("\n Tentando deletar...", end=" ")
    delete_query = sqlalchemy.text("delete from tb_book_sellers where dt_ref = :date")
    con.execute(delete_query, {"date": date_ref})
    con.commit()
    print("ok.")
except:
    print("Tabela não encontrada!")

try:
    print("\n Tentando criar tabela...", end=" ")
    create_query = sqlalchemy.text(f"create table tb_book_sellers as\n {query}")
    con.execute(create_query)
    print("ok.")
except:
    print("\n Tabela já existente, inserindo dados...", end=" ")
    insert_query = sqlalchemy.text(f"insert into tb_book_sellers \n {query}")  
    con.execute(insert_query)
    con.commit()
    print("ok.")
    


