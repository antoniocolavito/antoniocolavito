import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

user = 'root'
password = '32267'
host = '127.0.0.1'
database = 'ecommerce'

def connection_database (user, password, host, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except  mysql.connector.errors.DatabaseError as db_error:
        print(db_error.msg)
        return None

def close_connection(connection):
    connection.close()

conn = connection_database(user, password, host, database)
cursor = conn.cursor()

db_connection_str = 'mysql+pymysql://root:32267@127.0.0.1/ecommerce'
db_connection = create_engine(db_connection_str)

def query(select, frm, join1=None, join2=None, where=None, groupby=None, orderby=None):
    stmt = 'select %s from %s ' % (select,frm)
    if join1 is not None:
        stmt = stmt + 'join %s ' % join1
    if join2 is not None:
        stmt = stmt + 'join %s ' % join2
    if where is not None:
        stmt = stmt + 'where %s ' % where
    if groupby is not None:
        stmt = stmt + 'group by %s ' % groupby
    if orderby is not None:
        stmt = stmt + 'order by %s' % orderby
    stmt = stmt + ';'
    return stmt

def datafrane (qsql):
    q = pd.read_sql(qsql,db_connection)
    return q

#QUERY 1 // Seleziono i record in cui l'indirizzo contiene la parola 'CASSE MULTIMEDIA SPEAKER 400W P.M.P.O.'
select = 'nome'
frm = 'prodotto'
join1 = None
join2 = None
where = "nome = 'CASSE MULTIMEDIA SPEAKER 400W P.M.P.O.'"
groupby = None
orderby = None

qsql1 = query(select,frm,join1,join2,where,groupby,orderby)
print(qsql1)
cursor.execute(qsql1)
q1 = cursor.fetchall()
print('Query 1: ', q1)
qpandas1 = datafrane(qsql1)
print('Query 1 in Pandas è:', qpandas1)

print("\n")

#QUERY 2 // Seleziono i record in cui l'indirizzo contiene la parola 'WEBCAM'
select = 'nome'
frm = 'categoria'
join1 = None
join2 = None
where = "nome = 'WEBCAM'"
groupby = None
orderby = None

qsql2 = query(select,frm,join1,join2,where,groupby,orderby)
print(qsql2)
cursor.execute(qsql2)
q2 = cursor.fetchall()
print('Query 2: ', q2)
qpandas2 = datafrane(qsql2)
print('Query 2 in Pandas è:', qpandas2)

print("\n")

#QUERY 3 // Seleziono i prodotti con quantità disponibile
select = 'nome'
frm = 'prodotto'
join1 = None
join2 = None
where = 'quantita > 0'
groupby = None
orderby = None

qsql3 = query(select,frm,join1,join2,where,groupby,orderby)
print(qsql3)
cursor.execute(qsql3)
q3 = cursor.fetchall()
print('Query 3: ', q3)
qpandas3 = datafrane(qsql3)
print('Query 3 in Pandas è:', qpandas3)

print("\n")

#QUERY 4 // Seleziona i prodotti appartenenti alla marca HP
select = "prodotto.nome"
frm = "prodotto"
join1 = "marca on prodotto.mid=marca.mid"
join2 = None
where = "marca.nome = 'HP'"
groupby = None
orderby = None

qsql4 = query(select,frm,join1,join2,where,groupby,orderby)
print(qsql4)
cursor.execute(qsql4)
q4 = cursor.fetchall()
print('Query 4: ', q4)
qpandas4 = datafrane(qsql4)
print('Query 4 in Pandas è:', qpandas4)

#QUERY 5 // Seleziono gli utenti appartenenti alla provincia di Milano
select = 'nome, cognome'
frm = 'indirizzo'
join1 = None
join2 = None
where = "provincia = 'Milano'"
groupby = None
orderby = None

qsql5 = query(select,frm,join1,join2,where,groupby,orderby)
print(qsql5)
cursor.execute(qsql5)
q5 = cursor.fetchall()
print('Query 5: ', q5)
qpandas5 = datafrane(qsql5)
print('Query 5 in Pandas è:("\n")', qpandas5)


