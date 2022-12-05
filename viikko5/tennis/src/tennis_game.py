class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1
    

    def tie(self, player1_score):
        if player1_score == 0:
            score = "Love-All"
        elif player1_score == 1:
            score = "Fifteen-All"
        elif player1_score == 2:
            score = "Thirty-All"
        elif player1_score == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        return score
    

    def advantage_or_win(self,player_score_difference):
        if player_score_difference == 1:
            score = "Advantage player1"
        elif player_score_difference == -1:
            score = "Advantage player2"
        elif player_score_difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def other_game_states(self, player1_score, player2_score):
        score = self.get_player_score(player1_score) + "-" + self.get_player_score(player2_score)
        return score
    
    
    def get_player_score(self,player_score):
        if player_score == 0:
            score = "Love"
        elif player_score == 1:
            score = "Fifteen"
        elif player_score == 2:
            score = "Thirty"
        elif player_score == 3:
            score = "Forty"
        return score



    def get_score(self):
        game_score = ""

        if self.player1_score == self.player2_score:
            game_score = self.tie(self.player1_score)
   
        elif self.player1_score >= 4 or self.player2_score >= 4:
            player_score_difference = self.player1_score - self. player2_score
            game_score = self.advantage_or_win(player_score_difference)

        else:
            game_score = self.other_game_states(self.player1_score, self.player2_score)

        return game_score
