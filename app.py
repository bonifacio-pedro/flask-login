from flask import Flask, url_for, redirect, request, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import User

app = Flask(__name__)
engine = create_engine('mysql+mysqldb://root:45093988rgftqj@localhost/flasklogin', pool_recycle=3600)
Session = sessionmaker(bind=engine) # O session é o ponteiro, que envia dados a engine que se comunica com o DB
session = Session() # Criando ponteiro

@app.route("/")
def index():
    user = "Pedro"
    return render_template('index.html', user=user)

@app.route("/sign")
def sign():
    return render_template("sign.html")

@app.route("/sign", methods=['POST'])
def sign_add_user():
    if request.method == 'POST':
        user = User(username=request.form['username'],passwd=request.form['passwd'])
        session.add(user)
        session.commit()
        return redirect(url_for('index'))

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)