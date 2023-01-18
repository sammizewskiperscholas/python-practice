import mysql.connector as mariadb

con = mariadb.connect(
                    host="localhost",
                    user="root",
                    password="password",
                    database="test_db")

print("Successfully connected to MariaDB")

cur = con.cursor()

def generate_user_table():
    st="CREATE TABLE IF NOT EXISTS user_table( \
        email varchar(100), \
        name varchar(50), \
        password varchar(30) ) "
    cur.execute(st)
    print("Created table user_table")

    st="INSERT INTO user_table (email, name, password) \
        VALUES ('ywbaek@perscholas.org', 'young', 'letsgomet'), \
        ('mcordon@perscholas.org', 'marcial', 'perscholas'), \
        ('mhaseeb@perscholas.org', 'haseeb', 'platform') "
    cur.execute(st)
    print("Inserted 3 records...")
    #con.commit()

def get_all_users():
    st="SELECT * FROM user_table"
    cur.execute(st)
    print(cur.fetchall())

def get_user_by_name(name):
    st="SELECT * FROM user_table WHERE name = '{}'".format(name)
    cur.execute(st)
    print(cur.fetchall())

def validate_user(email,password):
    st="SELECT name FROM user_table \
        WHERE email = '{}' and password ='{}' \
        ".format(email,password)
    cur.execute(st)
    result = cur.fetchall()
    print(result)
    if result == []:
        print("Invalid user!")
        return False
    print("Valid user {}!".format(email))
    return True

def update_user(email, name, password):
    get_all_users()
    st="SELECT * FROM user_table WHERE \
        email = '{}'".format(email)
    cur.execute(st)
    result = cur.fetchall()
    print("update function")
    print(result)
    if result == []:
        return False
    else:
        st="UPDATE user_table \
            SET name = '{}', \
            password = '{}' \
            WHERE email = '{}' \
            ".format(name, password, email)
        cur.execute(st)
        get_all_users()
        return True

generate_user_table()
get_all_users()
get_user_by_name("young")
#print(validate_user('mhaseeb@perscholas.org','platform'))
print(validate_user('abc','platform'))
print(update_user('a', 'b', 'c'))
print(update_user('ywbaek@perscholas.org', 'youngymbaek', 'letsgometymbaek'))

con.commit()
con.close()





