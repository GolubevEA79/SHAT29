import sqlite3
DB_NAME="users.db"
def create_database():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS role(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role VARCHAR(25)
                    )          
                """)    
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login VARCHAR(25),
                    password VARCHAR(32),
                    role_fk INTEGER,
                    FOREIGN KEY (role_fk) REFERENCES role(id) ON DELETE CASCADE
                    )          
                """)
 
    connect.commit()
    cursor.close()
#create_database()
def insert_ints():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    roles=[('Администратор',),
        ('Модератор',),
        ('Пользователь',),
        ('Гость',)]


        #INSERT INTO role (role) VALUES('Admin');
    for role in roles:
            cursor.execute("""
                                INSERT INTO role (role)
                                VALUES(?)
            """,role)
    #connect.commit()
    #cursor.close()



    # users=[("user1","Pass1",1),
    #         ("user2","Pass2",1),
    #         ("user3","Pass3",1),
    #         ("user4","Pass4",1),
    #         ("user5","Pass5",1),
    #         ("user6","Pass6",1),
    #         ("user7","Pass7",1),    
    # ]
    # for user in users:
    #         cursor.execute("""
    #                             INSERT INTO users (login,password,role_fk)
    #                             VALUES(?,?,?)
    #         """,user)
#     connect.commit()
#     cursor.close()    
# insert_ints()
def select():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        SELECT login,password,role_fk FROM users WHERE id=4
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0])
    connect.commit()
    cursor.close()  

#select()

def update():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        UPDATE users SET password="123454321" WHERE id<>4
    """)
    
    connect.commit()
    cursor.close()     

#update()
#select()

def delete():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        DELETE FROM role WHERE 1
    """)
    connect.commit()
    cursor.close()  

# delete()
# select()

def select_role():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        SELECT * FROM role WHERE 1
    """)
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows

def insert_user(login,password):
    
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute("""
            INSERT INTO users (login,password,role_fk)
            VALUES(?,?,3)
            """,(login,password))                
    connect.commit()
    cursor.close()
    return 1




def select_user():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        SELECT * FROM users WHERE 1
    """)
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows


def select_avtoriz(login,password):
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        SELECT * FROM users WHERE login=? and password=?
    """,(login,password)
    )
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows