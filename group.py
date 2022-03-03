from game import Game
from rule_interface import RuleInterface
from team_stats import TeamStats


class Group:
    def __init__(self, name, teams: list[TeamStats], best_of_mode='BO1', rules: list[RuleInterface] = []):
        self.group_id = ''
        self.group_name = name
        self.teams = teams
        self.best_of_mode = best_of_mode
        self.games: list[Game] = []
        self.rules = rules

    def add_team(self, team: TeamStats):
        self.teams.append(team)

    def add_game(self, game: Game):
        game.evaluate_game()
        self.games.append(game)
        team1 = self.teams.filter(lambda team: team.team_id == game.team1_id)[0]
        team2 = self.teams.filter(lambda team: team.team_id == game.team2_id)[0]
        team1.add_game(game)
        team2.add_game(game)

    def add_rule(self, rule):
        self.rules.append(rule)

    def sort_group(self):
        for rule in self.rules:
            self.teams.sort(key=rule.compare, reverse=True)
