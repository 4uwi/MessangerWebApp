import mysql.connector as database

try:
    print('Attempting to connect to a database')
    Exception = database.connect(user='root', database='messenger', password='365841', host='localhost')
    print("Connected!")
except Exception:
    print('No database, creating!')
    with open('schema.sql') as f:
        connection = database.connect(user='root', password='365841')
        print('Executing creating script')
        connection.cursor().execute("CREATE DATABASE messenger")
        connection.cursor().execute("USE messenger")
        connection.cursor().execute(f.read())
        print('Database created')


connection = database.connect(user='root', database='messenger', password='365841', host='localhost')
cur = connection.cursor()

cur.execute("SHOW TABLES")
res = cur.fetchall()
print(res)
