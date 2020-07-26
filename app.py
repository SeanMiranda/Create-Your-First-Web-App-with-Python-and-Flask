from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/mydb'

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)