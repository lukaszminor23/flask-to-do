from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_bootstrap import Bootstrap


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
DB_NAME = "todo-list"

app = Flask(__name__)
app.config["SECRET_KEY"] = "dnsajdb basjkasbahbdjabdaj"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
Bootstrap(app)

db.init_app(app)
