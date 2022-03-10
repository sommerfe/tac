from game import Game
from group import Group
from match import Match
from team_stats import TeamStats
from tournament import Tournament
from game_rule import GameRule

def add_rule ():
    pass

def run_rules():
    pass

def add_team():
    pass

def create_team():
    pass

def create_group():
    pass



def main():
    print('Starting..')
    tournament = Tournament('Test Tournament', group_phase_best_of_mode='BO3')
    team1 = TeamStats('Team 1', '1')
    team2 = TeamStats('Team 2', '2')
    team3 = TeamStats('Team 3', '3')
    team4 = TeamStats('Team 4', '4')
    game_rule = GameRule('Test Rule')
    group = Group('Test Group', best_of_mode='BO3')
    group.add_rule(game_rule)
    group.add_team(team1)
    group.add_team(team2)
    group.add_team(team3)
    group.add_team(team4)
    tournament.add_group(group)
    game1 = Game(team1, team2, 0, 1, best_of_mode='BO3')
    # game2 = Game(team1, team3, 0, 1, best_of_mode='BO3')
    # game3 = Game(team4, team2, 0, 1, best_of_mode='BO3')
    # game4 = Game(team3, team4, 0, 1, best_of_mode='BO3')
    # game5 = Game(team1, team4, 0, 1, best_of_mode='BO3')
    # game6 = Game(team2, team3, 0, 1, best_of_mode='BO3')
    match1 = Match(team1, team2, team1)
    game1.add_match(match1)
    game1.add_match(match1)
    group.add_game(game1)
    # TODO add match to group to evaluate game after match is added
    # group.add_game(game2)
    # group.add_game(game3)
    # group.add_game(game4)
    # group.add_game(game5)
    # group.add_game(game6)
    group.sort_group()
    print('Finished.')
    print('tournament', str(tournament))
    print(str(group))



if __name__ == "__main__":
    main()