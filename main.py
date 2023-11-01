from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Adrian12\\Desktop\\Banco_Apex_Flask\\Banco\\Banco_BOD.sqlite3'
app.config['SECRET_KEY'] = 'senha_cripto'
db = SQLAlchemy(app)

from view import *

if __name__ == '__main__':
    app.run(debug=True)