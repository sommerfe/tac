from rule_interface import RuleInterface
from team_stats import TeamStats

class GameRule(RuleInterface):
    def __init__(self, name='Game Rule'):
        self.name = name

    def compare(self, team_stats1: TeamStats, team_stats2: TeamStats):
        return (team_stats1.wins - team_stats1.losses) - (team_stats2.wins - team_stats2.losses)
