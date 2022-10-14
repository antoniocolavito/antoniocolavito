import mysql.connector

conn = mysql.connector.connect(user='root', password='---', host='---', database='discografia')

cursor = conn.cursor()

sql= "insert into AUTORE (Nome, TitoloCanzone) VALUES ('%s', '&s')"




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

