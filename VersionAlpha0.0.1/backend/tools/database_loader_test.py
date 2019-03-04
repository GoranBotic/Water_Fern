import config
import psycopg2 as db
import sys
import os

#Connect to database
#TODO: add asymetric key auth
connection = db.connect(
    host        =   config.POSTGRES_ADDRESS,
    port        =   config.POSTGRES_PORT,
    database    =   config.POSTGRES_DB,
    user        =   config.POSTGRES_USER,
    password    =   config.POSTGRES_PASS
) 

#Generate cursor
cursor = connection.cursor()

def put_file(f,n):
    contents = f.read()
    cursor.execute("INSERT INTO "+config.TABLE_SUBMISSIONS+" (data,name,language) VALUES (%s,%s,%s)",(contents,n,"Java"))

for no, pe, files in os.walk(sys.argv[1]):
    for f in files:
        with open(sys.argv[1] + "/" + f, 'rb') as b:
            put_file(b,f)

connection.commit()
cursor.close()
connection.close()