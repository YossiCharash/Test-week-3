from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy
class Team:
    id = db.Column(db.Integer, primary_key=True)
    name_team = db.Column(db.String(50))
    PG_id = db.Column(db.Integer, nullable=True)
    SG_id = db.Column(db.Integer, nullable=True)
    SF_id = db.Column(db.Integer, nullable=True)
    PF_id = db.Column(db.Integer, nullable=True)
    c_id = db.Column(db.Integer, nullable=True)

