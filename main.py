from flask import Flask, redirect,request,render_template,url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/catalog')
def catalog():
    products=[[1,'Видеокарты',2,'Мат. платы']]
    return render_template('catalog.html',products=products)
@app.route('/add')
def add():
    return render_template('add.html')
if __name__=='__main__':
    app.run()