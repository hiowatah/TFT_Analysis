from API_Key import key
import requests, sqlite3

leagues = ['IRON', 'BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'DIAMOND']
divisions = ['I', 'II', 'III', 'IV']

connection = sqlite3.connect("Summoner_Info.db")
cursor = connection.cursor()

cursor.execute("""
                CREATE TABLE Summoner (
                leagueId TEXT,
                queueType TEXT,
                tier TEXT,
                rank TEXT,
                summonerId TEXT PRIMARY KEY,
                summonerName TEXT,
                leaguepoints INTEGER,
                wins INTEGER,
                losses INTEGER,
                veteran BOOLEAN,
                inactive BOOLEAN,
                freshBlood BOOLEAN,
                hotStreak BOOLEAN
                ) """)

def player_collector(key):
    summoner = {}
    for league in leagues:
        for division in divisions:
            response = requests.get(
            "https://na1.api.riotgames.com/tft/league/v1/entries/{}/{}?api_key={}".format(league, division, key))

            for user in response.json():
                cursor.execute("""
                                INSERT INTO TABLE Summoner (
                                leagueID, queueType, tier, rank, summonerId,
                                summonerName, leaguepoints, wins, losses, veteran,
                                inactive, freshBlood, hotStreak
                                )
                                VALUES (
                                %(leagueId)s,
                                %(queueType)s,
                                %(tier)s,
                                %(rank)s,
                                %(summonerId)s,
                                %(summonerName)s,
                                %(leaguepoints)s,
                                %(wins)s,
                                %(losses)s,
                                %(veteran)s,
                                %(inactive)s,
                                %(fresh)s,
                                %(hotStreak)s
                                )""", user)

    cursor.commit()
    cursor.close();

def puuid_collector(summoner):
    pass;
