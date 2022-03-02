class Match:
    def __init__(self, team1, team2):
        self.team1_id = team1
        self.team2_id = team2
        self.winner = None
        self.draw = False
        self.id = ''
    
    def set_winner(self, winner_id):
        self.winner = winner_id
