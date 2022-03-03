from team_stats import TeamStats

class RuleInterface:
    # def __init__(self, name, rule_type, rule_value):
    #     self.name = name
    #     self.rule_type = rule_type
    #     self.rule_value = rule_value
    #     self.rule_id = ''

    # def __str__(self):
    #     return '{} {} {}'.format(self.name, self.rule_type, self.rule_value)
    def compare(self, team_stats1: TeamStats, team_stats2: TeamStats) -> bool:
        pass