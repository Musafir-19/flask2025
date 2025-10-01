from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
db = SQLAlchemy()
app.config.from_object(Config)
migrate = Migrate(app, db)
db.init_app(app)

from school import routes, models