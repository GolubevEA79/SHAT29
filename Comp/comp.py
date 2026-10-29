from flask import Flask, redirect,request,render_template,url_for,jsonify,session
from db import select_user, select_client, select_component, select_unit, select_texnik
app = Flask(__name__)

app.json.ensure_ascii=False
app.config["SESSION_COOKIE_HTTPONLY"]=True# передает куки только по https
app.config["SESSION_COOKIE_SAMESITE"]="Lax"
app.secret_key = '12345'

@app.route('/clients')
def clients():
    clients=select_client()
    return render_template('client.html', clients=clients)

@app.route('/components')
def components():
    components=select_component()
    return render_template('component.html', components=components)

@app.route('/users')
def users():
    users=select_user()
    return render_template('user.html', users=users)

@app.route('/texnika')
def texnika():
    texnika=select_texnik()
    return render_template('texnik.html', texnika=texnika)

@app.route('/units')
def units():
    units=select_unit()
    return render_template('unit.html', units=units)

if __name__=='__main__':
    app.run()