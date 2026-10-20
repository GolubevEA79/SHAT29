from flask import Flask, redirect,request,render_template,url_for,jsonify,session
from db import select_role, insert_user, select_user, select_avtoriz
app = Flask(__name__)

app.json.ensure_ascii=False
app.config["SESSION_COOKIE_HTTPONLY"]=True# передает куки только по https
app.config["SESSION_COOKIE_SAMESITE"]="Lax"
app.secret_key = '1211'


products=[
        {"id":1,"name":'Видеокарты'},
        {"id":2,"name":'Мат. платы'}
        ]

users={
    "login":"admin",
    "password":"12345"
    }



@app.route('/')

def index():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template('index.html')
app.json.ensure_ascii=False
@app.route('/catalog')
def catalog():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template('catalog.html',products=products)
@app.route('/add')
def add():
    if "user_id" not in session:
        return redirect(url_for("login"))    
    return render_template('add.html')

@app.route('/reg')
def reg():
    return render_template('registration.html')
@app.route('/api/reg',methods=['POST'])
def api_reg():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    
    if not login or not password: #or net role:   
       return jsonify({
            "success":False,
            "message":"Введите логин и пароль"
        }),400
    reg = insert_user(login,password)

    if reg==1:
       return jsonify({
            "success":True,
            "message":"Регистрация успешна",
            "redirect":url_for('login')
        }),201
    else:
        return jsonify({
                "success":True,
                "message":"Регистрация не успешна",
                "redirect":url_for('reg')
            }),201     

def api_login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    role = data.get('role')
    if not login or not password: #or net role:   
       return jsonify({
            "success":False,
            "message":"Введите логин и пароль"
        }),400
    reg = insert_user(login,password)

    if reg==1:
       return jsonify({
            "success":True,
            "message":"Регистрация успешна",
            "redirect":url_for('login')
        }),201
    else:
        return jsonify({
                "success":True,
                "message":"Регистрация не успешна",
                "redirect":url_for('reg')
            }),201  

#    return 1


@app.route('/api/products',methods=['GET'])
def api_products():
    return jsonify(products)

@app.route('/api/products/<int:id>',methods=['GET'])
def api_product(id):
    for product in products:
        if product["id"]==id:
            return jsonify(product)
    return jsonify({'error':f"Товар {id} не найден"})


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/api/login',methods=['POST'])
def api_login():
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')
    user=select_avtoriz(login,password)

# print(select_avtoriz(login,password))

    if not isinstance(login,str) or not isinstance(password,str):
        return jsonify({
            "success":False,
            "message":"Введите логин и пароль"
        }),400
    
    if len(user)!=0:

        session.clear()
        session["user_id"]=user[0]

        return jsonify({
            "success":True,
            "message":"Авторизация успешна",
            "redirect":url_for('catalog')
        }),201
    else:
        return jsonify({
                "success":False,
                "message":"Авторизация не успешна",
                "redirect":url_for('login')
            }),201    
#    return None

if __name__=='__main__':
    app.run()