from flask import Blueprint, jsonify, request
from db import db
from data_base.player_db import Player


players = Blueprint('players', __name__)


def add_ATR():
    players = Player.query.all()
    for player in players:
        if player.turnovers != 0 and player.assists != 0:
            player.ATR = create_ATR(player.assists, player.turnovers)
        else:
            player.ATR = 0
    db.session.commit()
    return [{'playerID': player.playerId, } for player in players]

#calculate the ATR
def create_ATR(assists,turnovers):
    ATR = assists / turnovers
    return ATR



@players.route('/playerss?position={position}&season={season}',methods=['GET'])
def get_all_players_position(season,position):
    players = Player.query.all()

    for player in players:
        #the filter all
        filter_season = filter(lambda p: p.season == season, players)
        filter_position = filter(lambda p: p.position == position, filter_season)


        #the list for points
        points_position_all = [x.points for x in filter_position]


        #the calcul the one player
        average_all = len(points_position_all) / sum(points_position_all)
        filter_plye_by_plyer_id = filter(lambda p: p.player_id == players[0].playerId, players)


        points_by_plyer = [x.points for x in filter_plye_by_plyer_id if x.points == player.points]
        average_by_plyaer = len(points_by_plyer) / sum(points_by_plyer)

        #the update db
        player.create_PPG(average_by_plyaer / average_all)
        db.session.commit()
    return [{'playerID': player.PPG_Ratio, } for player in players],200



