from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from team_db import db
from team_db import Team
teams = Blueprint('teams', __name__)
import requests


@teams.route('/teams', methods=['POST'])
def create_temp():
    data = request.get_json()
    new_team = Team(name_team=data['name_team'],PG_id=data['PG_id'], SG_id=data['SG_id'], SF_id=data['SF_id'], PF_id=data['PF_id'], c_id=data['c_id'])
    try:
        db.session.add(new_team)
        db.session.commit()
        return jsonify({'messege': "the user  is created"}),201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({'messege': "the user  is already created"}),201



def generate_teams_responce(teams=None, team=None):
    if teams:
        return [{'teamname': team.name_team,} for team in teams]
    elif team:
        return {'username': team.username}



# get all users
@teams.route('/teams/<int:team_id>', methods=['GET'])
def get_users(team_id):
    teams = Team.query.filter(Team.id == team_id).all()
    if teams:
        team_responce = generate_teams_responce(teams=teams)
        print(team_responce)
        return jsonify(team_responce), 200
    else:
        return jsonify({"error": "I not pound the users: "}), 404


