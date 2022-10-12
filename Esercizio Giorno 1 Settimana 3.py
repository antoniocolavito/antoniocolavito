import mysql.connector

conn = mysql.connector.connect(user='root', password='32267', host='127.0.0.1', database='discografia')

cursor = conn.cursor()

sql= "insert into AUTORE (Nome, TitoloCanzone) VALUES ('Paolo Conte', 'Via con me')"




try:
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()


query_stmt= 'SELECT * FROM autore'

cursor.execute(query_stmt)    #eseguo l'interrogazione al cursore che diventerà accessibile tramite fetch
result=cursor.fetchall()
print('Nome' , result, 'TitoloCanzone',result )


def close_connetion (connection):
    connection.close()

def trying(sql):
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

    except:
        conn.rollback()


def add_delete(sql):

    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()

