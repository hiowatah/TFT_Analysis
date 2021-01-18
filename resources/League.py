from flask_restful import Resource
from models.League import LeagueModel

class League(Resource):
    def get(self, summonerName):
        league = LeagueModel.find_by_name(summonerName)
        if league:
            return league.json()
        return {'message': "Summoner not found"}, 404

    def post(self, summonerName):
        

    def delete(self, summonerName):
        pass


class LeagueList(Resource):
    def get(self):
        return {"leagues": [league.json() for league in LeagueModel.query.all()]}
