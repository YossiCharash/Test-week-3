from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy
class Team:
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    name_team = db.Column(db.String(50), nullable=False)
    PG_id = db.Column(db.String, nullable=True)
    SG_id = db.Column(db.String, nullable=True)
    SF_id = db.Column(db.String, nullable=True)
    PF_id = db.Column(db.String, nullable=True)
    C_id = db.Column(db.String, nullable=True)

