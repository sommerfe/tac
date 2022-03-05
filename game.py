from match import Match
from team_stats import TeamStats


class Game:
    def __init__(self, team1: TeamStats, team2: TeamStats, team1_score=0, team2_score=0, best_of_mode='BO1'):
        self.team1: TeamStats = team1
        self.team2: TeamStats = team2
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.best_of_mode = best_of_mode
        self.winner = None
        self.draw = False
        self.id = ''
        self.evaluate_game()

    def get_stats_for_player (self, player_id):
        if player_id == self.team1.team_id:
            return self.team1_score, self.team2_score
        else:
            return self.team2_score, self.team1_score

    def add_match (self, match: Match):
        winner = match.winner
        if winner == self.team1:
            self.team1_score += 1
        elif winner == self.team2:
            self.team2_score += 1
        
        if self.is_last_match():
            self.evaluate_game()

    def evaluate_game (self):
        if self.team1_score > self.team2_score:
            self.winner = self.team1
        elif self.team1_score < self.team2_score:
            self.winner = self.team2
        elif self.team1_score <= 0 and self.team2_score <= 0:
            self.draw = None
        else:
            self.draw = True
            self.winner = None

    def is_last_match (self):
        if self.best_of_mode == 'BO1':
            return self.team1_score >= 1 or self.team2_score >= 1
        elif self.best_of_mode == 'BO3':
            return self.team1_score >= 2 or self.team2_score >= 2
        elif self.best_of_mode == 'BO5':
            return self.team1_score >= 3 or self.team2_score >= 3
        elif self.best_of_mode == 'BO7':
            return self.team1_score >= 4 or self.team2_score >= 4
        elif self.best_of_mode == 'BO9':
            return self.team1_score >= 5 or self.team2_score >= 5
        else:
            return False