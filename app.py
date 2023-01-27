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
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)