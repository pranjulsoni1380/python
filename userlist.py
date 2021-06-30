import pymysql

con = pymysql.connect('database-1.cy1jk3ql5lqn.ap-south-1.rds.amazonaws.com', 'admin',
    'YHHfHhGL1380')

try:

    with con.cursor() as cur:

        cur.execute('SELECT user FROM mysql.user')

finally:

    con.close()
