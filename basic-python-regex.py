import mysql.connector as mariadb

con = mariadb.connect(
                    host="localhost",
                    user="root",
                    password="password",
                    database="classicmodels")

print("Successfully connected to MariaDB")

cur = con.cursor()

st = "SELECT productline, count(*) \
        FROM products WHERE productline='{}'"
cur.execute(st.format('Motorcycles'))
print(cur.fetchall())
con.close()
con = mariadb.connect(
                    host="localhost",
                    user="root",
                    password="password")
print("Connected to MAriaDB database...")
cur = con.cursor()

st = "CREATE DATABASE test_db"
cur.execute(st)
print("test_db is created")
con.close()