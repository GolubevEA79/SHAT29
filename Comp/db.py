# Создание базы данных
import sqlite3
DB_NAME="compservis.db"
def create_database():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS clients(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fio VARCHAR(50)
                    )          
                """)    
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS texnika(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50) 
                    )         
                """)
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fio VARCHAR(50),
                    pass VARCHAR(25)
                    )          
                """)

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS components(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50),
                    price VARCHAR(10)
                    )          
                """)
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS units(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50),
                    price VARCHAR(10)
                    )         
                """)
 
    connect.commit()
    cursor.close()
#create_database()

# Заполнение данными таблицы users
def insert_ints():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    users=[("Иванов Петр Сергеевич","ИПС"),
        ("Строев Иван Андреевич","СИА"),
        ("Пришвин Максим Александрович","ПМА"),
        ("Карушев Андрей Владимирович","КАВ")]
    for user in users:
        cursor.execute("""
                        INSERT INTO users (fio,pass)
                        VALUES(?,?)
                    """,user)
    connect.commit()
    cursor.close()
#insert_ints()

# Заполнение данными таблицы clients
def insert_ints():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    clients=[("ФИО1",),
        ("ФИО2",),
        ("ФИО3",),
        ("ФИО4",),
        ("ФИО5",),
        ("ФИО6",),
        ("ФИО7",),
        ("ФИО8",),
        ("ФИО9",)]
    for client in clients:
        cursor.execute("""
                        INSERT INTO clients (fio)
                        VALUES(?)
                    """,client)
    connect.commit()
    cursor.close()
#insert_ints()

#Заполнение данными таблицы components
def insert_ints():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    components=[("Screen","1500rub"),
           ("Battery","1000rub"),
           ("Button","500rub"),
           ("Monitor","10 000rub"),
    ]
    for component in components:
            cursor.execute("""
                INSERT INTO components(name, price)
                VALUES(?,?)
                            
            """,component)
    connect.commit()
    cursor.close()
#insert_ints()

#Заполнение данными таблицы units
def insert_ints():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    units=[("repair","1500rub"),
           ("changes","1000rub"),
           ("utilization","500rub"),
           
    ]
    for unit in units:
            cursor.execute("""
                INSERT INTO units(name, price)
                VALUES(?,?)
                            
            """,unit)
    connect.commit()
    cursor.close()
#insert_ints()

#Заполнение данными таблицы texnika
def insert_ints():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    texnika=[("Монитор",),
           ("Принтер",),
           ("Картридж",),
           ("Роутер",),
           ("Сканер",),
           
    ]
    for texnik in texnika:
            cursor.execute("""
                INSERT INTO texnika(name)
                VALUES(?)
                            
            """,texnik)
    connect.commit()
    cursor.close()
#insert_ints()

#Выбор данных из таблиц
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

def select_client():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        SELECT * FROM clients WHERE 1
    """)
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows

def select_component():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        SELECT * FROM components WHERE 1
    """)
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows

def select_unit():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        SELECT * FROM units WHERE 1
    """)
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows

def select_texnik():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()   
    cursor.execute("""
        SELECT * FROM texnika WHERE 1
    """)
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows

