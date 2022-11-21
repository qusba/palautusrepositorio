import requests
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.get_players())
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)
main()