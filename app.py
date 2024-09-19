from flask import Flask, jsonify, request, abort
from sqlalchemy.util import await_only

from data_base.player_db import Player
import requests
from sqlalchemy.exc import IntegrityError
from db import db
from data_base.route import players
from db import url_S

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playre.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def hello_world():  # put application's code here
    return

db.init_app(app)


with app.app_context():
    url_S()
    db.create_all()

@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    return jsonify({'error': "Duplicate email or missing data"}), 400
app.register_blueprint(players)


if __name__ == '__main__':

    app.run()

