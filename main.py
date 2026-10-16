from flask import Flask, redirect,request,render_template,url_for,jsonify
app = Flask(__name__)
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
    return render_template('index.html')
app.json.ensure_ascii=False
@app.route('/catalog')
def catalog():

    return render_template('catalog.html',products=products)
@app.route('/add')
def add():
    return render_template('add.html')

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
    if not isinstance(login,str) or not isinstance(password,str):
        return jsonify({
            "success":False,
            "message":"Введите логин и пароль"
        }),400
    if login==users['login'] and password== users['password']:
        return jsonify({
            "success":True,
            "message":"Авторизация успешна",
            "redirect":url_for('catalog')
        })
    return None

if __name__=='__main__':
    app.run()