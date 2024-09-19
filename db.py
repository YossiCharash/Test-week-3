from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from data_base import player_db

import requests


URL_NBA_2024 = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2024&&pageSize=1000"
URL_NBA_2023 = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2023&&pageSize=1000"
URL_NBA_2022 = "http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season=2022&&pageSize=1000"


def read_url_to_json(url):
    responses = requests.get(url).json()
    for player in responses:
        create_player_to_db(player)


def url_S():
    read_url_to_json(URL_NBA_2024)
    read_url_to_json(URL_NBA_2023)
    read_url_to_json(URL_NBA_2023)
    return

def create_player_to_db(player: dict):

    new_player = player_db.Player(
        playerName=['playerName'], playerId=player['playerId'],
        team=player['team'], position=player['position'],
        points=player['points'], season=player['season'],
        twoPercent=player['twoPercent'], threePercent=player['threePercent'],
        turnovers=player['turnovers'], assists=player['assists']
    )
    db.session.add(new_player)
    db.session.commit()
