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
    """
    Verificando se existe uma sessão de login ativa, se sim, enviando ao HTML para verificação de conteudo mostrado
    """
    if 'user_loged' in ss:
        user = ss['user_loged'] # Pegando nome do user em sessão
        return render_template('index.html', user_loged=user)
    else:
        return render_template('index.html')

#
# Área de cadastro 
#
@app.route("/sign")
def sign():
    if not 'user_loged' in ss:
        return render_template("sign.html")
    else:
        return redirect(url_for('index'))

@app.route("/sign", methods=['POST'])
def sign_add_user():
    """
    Adicionando cadastro ao banco de dados
    """
    if request.method == 'POST':
        user = User(username=request.form['username'],passwd=request.form['passwd'])
        session.add(user)
        session.commit()
        ss['user_creating'] = True
        return redirect(url_for('login'))

#
# Área de login
#
@app.route("/login")
def login():
    if not 'user_loged' in ss:
        if 'user_creating' in ss:
            return render_template("login.html", in_creation=ss['user_creating'])
        else:
            return render_template("login.html")
    else:
        return redirect(url_for("index"))

@app.route("/login", methods=['POST'])
def login_verify_user():
    """
    Verificando e procurando o username requirido no banco de dados, se tiver, verificar a senha utilizando o hash e redirecionando com uma nova sessão aberta.
    """
    if request.method == 'POST':
        user = session.query(User).filter_by(username=request.form['username']).first()
        if user and user.verify_passwd(request.form['passwd']):
            ss['user_loged'] = user.username
            ss.pop('user_creating', None)
            return redirect(url_for('index'))
        else:
            return render_template("login.html", is_logged=True)

#
# Área de logout
#
@app.route("/logout")
def logout():
    ss.pop('user_loged',None) # Apenas fechando a sessão, modificando a variável para None
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)