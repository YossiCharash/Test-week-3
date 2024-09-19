from db import db

# db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    playerName = db.Column(db.String(80), nullable=True)
    team =db.Column(db.String(80), nullable=True)
    position = db.Column(db.String(80), nullable=True)
    points = db.Column(db.Integer, nullable=True)
    season = db.Column(db.Integer, nullable=True)
    twoPercent = db.Column(db.Double, nullable=True)
    threePercent = db.Column(db.Double, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    playerId = db.Column(db.String(80), nullable=True)
    ATR = db.Column(db.Integer, nullable=True)
    PPG_Ratio = db.Column(db.Integer, nullable=True)

    def __str__(self):
        return  (self.playerName,
                 self.team,
                 self.position,
                 self.points,
                 self.season,
                 self.twoPercent,
                 self.threePercent,
                 self.ATR,
                 )




    def create_PPG(self,ppg):
        self.PPG_Ratio = ppg
        db.session.commit()
        db.session.refresh(self)





