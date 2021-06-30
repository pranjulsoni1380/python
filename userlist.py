import pymysql

con = pymysql.connect('dev-test-v2-app-mysql.cwspxlo5k4ke.us-west-2.rds.amazonaws.com', 'MYSQL_USERNAME',
    'MYSQL_PASSWORD')

try:

    with con.cursor() as cur:

        cur.execute('SELECT user FROM mysql.user')

finally:

    con.close()
