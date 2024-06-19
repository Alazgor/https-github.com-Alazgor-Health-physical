from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# Инициализация Flask приложения
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация Bootstrap расширения
bootstrap = Bootstrap(app)

# Инициализация SQLAlchemy
db = SQLAlchemy(app)

# Инициализация Flask-Migrate
migrate = Migrate(app, db)

# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

# Импорт маршрутов после инициализации app, db и login_manager
from app import routes
