from group import Group


class Tournament:
    def __init__(self, name, groups: list[Group] = [], group_phase_best_of_mode='BO1'):
        self.tournament_id = ''
        self.tournament_name = name
        self.groups = groups
        self.group_phase_best_of_mode = group_phase_best_of_mode
    
    def add_group(self, group):
        self.groups.append(group)

