
class PlayerStats():
    def __init__(self,list_of_players):
        self.players = list_of_players

    def top_scorers_by_nationality(self,nationality):
        top_scorers = []

        for player in self.players:
            if player.nationality == nationality:
                top_scorers.append(player)
        
        top_scorers = sorted(top_scorers,key=lambda player: player.goals + player.assists, reverse=True)

        return top_scorers