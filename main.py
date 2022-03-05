from game import Game
from group import Group
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
    tournament = Tournament('Test Tournament')
    team1 = TeamStats('Team 1', '1')
    team2 = TeamStats('Team 2', '2')
    team3 = TeamStats('Team 3', '3')
    team4 = TeamStats('Team 4', '4')
    game_rule = GameRule('Test Rule')
    group = Group('Test Group')
    # group.add_rule(game_rule)
    group.add_team(team1)
    group.add_team(team2)
    group.add_team(team3)
    group.add_team(team4)
    tournament.add_group(group)
    game = Game(team1, team2, 1, 0)
    group.add_game(game)
    group.sort_group()
    print('Finished.')
    print('tournament', str(tournament))
    print(str(group))



if __name__ == "__main__":
    main()