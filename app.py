from flask import Flask, url_for, redirect, request, render_template
from flask import session as ss
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import User

app = Flask(__name__)
app.secret_key = "169bd92c933cdff0f76235d16981ccc2" # Para sessão
engine = create_engine('mysql+mysqldb://root:45093988rgftqj@localhost/flasklogin', pool_recycle=3600)
Session = sessionmaker(bind=engine) # O session é o ponteiro, que envia dados a engine que se comunica com o DB
session = Session() # Criando ponteiro

@app.route("/")
def index():
    if 'user_loged' in ss:
        user = ss['user_loged']
        return render_template('index.html', user_loged=user)
    else:
        return render_template('index.html')

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

@app.route("/login", methods=['POST'])
def login_verify_user():
    if request.method == 'POST':
        user = session.query(User).filter_by(username=request.form['username']).first()
        if user and user.verify_passwd(request.form['passwd']):
            ss['user_loged'] = user.username
            return redirect(url_for('index'))
        else:
            return render_template("login.html", is_logged=True)

@app.route("/logout")
def logout():
    ss.pop('user_loged',None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)