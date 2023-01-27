from flask import Flask, url_for, redirect, request, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import User

app = Flask(__name__)
engine = create_engine('mysql+mysqldb://root:45093988rgftqj@localhost/flasklogin', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)