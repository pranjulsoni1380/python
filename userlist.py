#!/usr/bin/python3


import pymysql
import sys

args=

con = pymysql.connect('database-1.cy1jk3ql5lqn.ap-south-1.rds.amazonaws.com', 'MYSQL_USERNAME',
    'MYSQL_PASSWORD')

try:

    with con.cursor() as cur:

        cur.execute('SELECT user FROM mysql.user')
        result = cur.fetchall()
        print(result)

finally:

    con.close()
