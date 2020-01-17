from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('game_app.config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
import game_app.views
