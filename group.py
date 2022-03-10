from game import Game
from rule_interface import RuleInterface
from team_stats import TeamStats
import functools

def compare(team_stats1: TeamStats, team_stats2: TeamStats):
    # print('compare', team_stats1.team_name, team_stats2.team_name, (team_stats1.wins - team_stats1.losses) - (team_stats2.wins - team_stats2.losses))
    return (team_stats1.wins - team_stats1.losses) - (team_stats2.wins - team_stats2.losses)
    # if team_stats1.wins > team_stats2.wins:
    #     return -1
    # elif team_stats1.wins < team_stats2.wins:
    #     return 1
    # else:
    #     return 0
class Group:
    def __init__(self, name, teams=[], best_of_mode='BO1', rules = []):
        self.group_id = ''
        self.group_name = name
        self.teams: list[TeamStats] = teams
        self.best_of_mode = best_of_mode
        self.games: list[Game] = []
        self.rules: list[RuleInterface] = rules

    def add_team(self, team: TeamStats):
        self.teams.append(team)

    def add_game(self, game: Game):
        game.evaluate_game()
        self.games.append(game)
        # team1: TeamStats = self.teams.filter(lambda team: team.team_id == game.team1_id)[0]
        team1: TeamStats = next((team for team in self.teams if team.team_id == game.team1.team_id), None)
        team2: TeamStats = next((team for team in self.teams if team.team_id == game.team2.team_id), None)
        # team2: TeamStats = self.teams.filter(lambda team: team.team_id == game.team2_id)[0]
        self.add_game_to_teams(team1, team2, game)
        # team1.add_game(game)
        # team2.add_game(game)


    def add_game_to_teams(self, team1: TeamStats, team2: TeamStats, game: Game):
        if game.winner == team1:
            team1.wins += 1
            team2.losses += 1
        elif game.winner == None:
            team1.ties += 1
            team2.ties += 1
        else:
            team1.losses += 1
            team2.wins += 1
        team1.points_for += game.team1_score
        team2.points_for += game.team2_score
        team1.points_against += game.team2_score
        team2.points_against += game.team1_score



    def add_rule(self, rule):
        self.rules.append(rule)
        # pass

    def sort_group(self):
        for rule in self.rules:
            self.teams.sort(key=functools.cmp_to_key(rule.compare), reverse=True)
        # pass
        # self.teams.sort(key=compare)
        # self.teams.sort(key=lambda team: team.wins, reverse=True)
        # sorted(self.teams, key=functools.cmp_to_key(compare))
        # self.teams.sort(key=functools.cmp_to_key(compare), reverse=True)

    def __str__(self):
        start = '----------------------------------------\n'
        header = 'Team ---- W ---- L ---- Pts For ---- Pts Against ---- Win % ---- Pts Diff ---- Pts Diff %\n'
        tea = ['{} ---- {} ---- {} ---- {} ---- {} ---- {} ---- {} ---- {}'.format(team.team_name, team.wins, team.losses, team.points_for, team.points_against, team.win_percentage, team.points_difference, team.points_difference_percentage) for team in self.teams]
        separator = '\n'
        teas = separator.join(tea)
        end = '\n----------------------------------------'
        return '{}{}{}{}'.format(start, header, teas, end)

