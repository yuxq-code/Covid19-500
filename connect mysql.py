# How to use python to build database in mysql

# install mysql connector
import pymysql


# define function, global means “conn and cur” can be used everywhere
def conn_open():
    global conn, cur


# connect mysql
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='12345')

cursor = conn.cursor()

# build new database ab in mysql

cursor.execute("CREATE DATABASE ab")

# check all database in mysql
cursor.execute("SHOW DATABASES")

# print database one by one
databases = cursor.fetchall()
for database in databases:
    print(database)

# connect python to database “your_database_name”

import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='12345',
                       database='covid500',
                       charset='UTF8')
cursor = conn.cursor()

# build table in database your_database_name
cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")

# check table
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# print table one by one
for table in tables:
    print(table)


# close the database connection
def conn_close():
    cur.close()
    conn.close()
