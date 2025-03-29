from flask import Flask
from flask_mysqldb import MySQL
from flask_session import Session
from flask_caching import Cache
from app.config import Config

# Initialisation de l'application
app = Flask(__name__)
app.config.from_object(Config)

# Initialisation des extensions
mysql = MySQL(app)
session = Session(app)
cache = Cache(app)

# Importation des routes
from app.controllers import auth_controller