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


connection.commit()
connection.close()

# connection = database.connect(user='root', password='365841', database='messenger')
# cur = connection.cursor()
#
# cur.execute("SELECT * FROM message")
# res = cur.fetchall()
#
# cur.execute("SELECT * FROM message")
# res1 = cur.fetchone()
#
# print(res.__class__, res1.__class__)
