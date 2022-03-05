# from game import Game


class TeamStats:
    def __init__(self, name, team_id='', wins=0, losses=0, ties=0, points_for=0, points_against=0):
        self.team_id = team_id
        self.team_name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.points_for = points_for
        self.points_against = points_against
        self.win_percentage = 0 if self.wins == 0 else self.wins / (self.wins + self.losses + self.ties)
        self.points_difference = self.points_for - self.points_against
        self.points_difference_percentage = 0 if self.points_difference == 0 else self.points_difference / (self.points_for + self.points_against)
        # self.games: list[Game] = []

    # def add_game (self, game: Game):
    #     self.games.append(game)

    #     if game.winner == self:
    #         self.wins += 1
    #     elif game.winner == None:
    #         self.ties += 1
    #         self.points_for += game.team1_score
    #         self.points_against += game.team2_score
    #     else:
    #         self.losses += 1
    #         self.points_for += game.team2_score
    #         self.points_against += game.team1_score

    #     team1_score, team2_score = game.get_stats_for_player(self.team_id)
    #     self.points_for += team1_score
    #     self.points_against += team2_score
