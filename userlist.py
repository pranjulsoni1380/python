import pymysql

con = pymysql.connect('localhost', 'user7',
    's$cret', 'testdb')

try:

    with con.cursor() as cur:

        cur.execute('SELECT user FROM mysql.user')

finally:

    con.close()
