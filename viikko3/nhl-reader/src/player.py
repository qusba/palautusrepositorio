class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        
    def total(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} team {self.team} {self.goals} + {self.assists} = {self.goals + self.assists}"
