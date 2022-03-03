from rule_interface import RuleInterface
from team_stats import TeamStats

class GameRule(RuleInterface):
    def __init__(self, name='Game Rule'):
        self.name = name

    def compare(self, team_stats1: TeamStats, team_stats2: TeamStats) -> int:
        if team_stats1.wins > team_stats2.wins:
            return -1
        elif team_stats1.wins < team_stats2.wins:
            return 1
        else:
            return 0