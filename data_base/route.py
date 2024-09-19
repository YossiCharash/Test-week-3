import json

import requests
from flask import Blueprint, jsonify

from class_models.plaer_model import PlayerModel
from db import db
from data_base.player_db import Player


players = Blueprint('players', __name__)


@players.route('/players/all',methods=['GET'])
def get_all_players():
    players = Player.query.all()
    return jsonify(players)

# @players.route('/players/position=?<string:season>',methods=['GET'])
# def get_all_players_position(season):
#     players = Player.query.filter_by(season=season).all()
#
#     return jsonify(players)
#

