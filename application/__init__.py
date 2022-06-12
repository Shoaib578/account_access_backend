from flask import Flask
app = Flask(__name__)
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os 
from flask_cors import CORS 
app.config['SECRET_KEY'] = 'asjd9792nasd887a8dA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/account_access'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from flask_marshmallow import Marshmallow
ma= Marshmallow(app)

db = SQLAlchemy(app)
Migrate(app,db)
from flask_login import LoginManager
login_manager = LoginManager(app)
login_manager.login_view ="main.Login"
CORS(app)
from application.Main.routes import main
from application.Admin.routes import admin
from application.Apis.routes import apis
app.register_blueprint(main)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(apis,url_prefix="/apis")



