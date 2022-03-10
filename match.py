from team_stats import TeamStats


class Match:
    def __init__(self, team1, team2, winner=None):
        self.team1 = team1
        self.team2 = team2
        self.winner = winner
        self.draw = False
        self.id = ''
    
    def set_winner(self, winner: TeamStats):
        self.winner = winner
