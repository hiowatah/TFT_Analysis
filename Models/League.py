from db import db

class LeagueModel(db.Model):
    __tablename__ = 'league'

    summonerId = db.Column(db.String(80), primary_key=True)
    leagueid = db.Column(db.String(80))
    queuetype = db.Column(db.String(80))
    tier = db.Column(db.String(80))
    rank = db.Column(db.String(80))
    summonerName = db.Column(db.String(80))
    leaguepoints = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    losses = db.column(db.Integer)
    veteran = db.column(db.Boolean)
    inactive = db.column(db.Boolean)
    freshBlood = db.column(db.Boolean)
    hotStreak = db.column(db.Boolean)

    def __init__(self, leagueId, queuetype, tier, rank, summonerName, leaguepoints, wins, losses, veteran, inactive, freshBlood, hotStreak):
        self.leagueId = leagueId
        self.queuetype = queuetype
        self.tier = tier
        self.rank = rank
        self.summonerName = summonerName
        self.leaguepoints = leaguepoints
        self.wins = wins
        self.losses = losses
        self.veteran = veteran
        self.inactive = inactive
        self.freshBlood = freshBlood
        self.hotStreak = hotStreak

    def json(self):
        return 

    @classmethod
    def find_by_name(cls, summonerName):
        return cls.query.filter_by(name=summonerName).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
