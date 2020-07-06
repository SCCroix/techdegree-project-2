import constants

def add_player_to_team(player, team):
    player['team'] = team


def average_height_of_team(team, players):
    heights = []
    for player in team_players(team, players):
        heights.append(player["height"])
    return sum(heights) / len(heights)


def balance_teams(teams, players):
    """ Distributes players to teams """
    # Find number of players per team
    team_size = len(players) / len(teams)
    # Distribute players to teams
    exp_players = [player["name"] for player in players if player['experience'] == True]
    new_players = [player["name"] for player in players if player['experience'] == False]
    for team in teams:
        while number_players_on_team(team) < team_size:
            team["roster"].append(new_players.pop())
            team["roster"].append(exp_players.pop())


def convert_height_to_int(str):
    """ Convert the text height to an integer """
    return int(str.split()[0])


def convert_exp_to_bool(str):
    """ Converts 'YES' or 'NO' to true false """
    return str == "YES"


def convert_guardians_to_list(str):
    """ Converts str of 'player and player' to list """
    return str.split(" and ")


def display_menu():
    print("\n ____ Main Menu ____ \n")
    print("""
Here are your choices:
  1) Display Team Stats
  2) Quit
""")


def display_teams(teams):
    for number, team in enumerate(teams, 1):
        print(f'  {number}) {team["name"]}')


def display_team_stats(team_index, teams):
    team = teams[team_index]
    print(f'\n{team["name"]} stats\n')
    print(f'Total Players: {len(team["roster"])}')
    print(f'New Players: {num_new_players(team)}')
    print(f'Experienced Players: {num_exp_players(team)}')
    print(f'Players on team:\n   {", ".join(team["roster"])}')
    print(f'Team Guardians:\n   {", ".join(team_guardians(team, players))}')
    print(f'Average height: {average_height_of_team(team, players)}')


def clean_data(players):
    return [clean_player_data(player) for player in players]


def clean_player_data(player):
    clean_player_data = {}
    # Copy over name
    clean_player_data['name'] = player['name']
    # Change Guardians to list
    clean_player_data['guardians'] = convert_guardians_to_list(player['guardians'])
    # Change height to an integer
    clean_player_data['height'] = convert_height_to_int(player['height'])
    # Change experienced to true false
    clean_player_data['experience'] = convert_exp_to_bool(player['experience'])
    return clean_player_data


def get_option_from_user(integer):
    while True:
        response = input("Please select a number from above: ")
        try:
            response = int(response)
        except ValueError:
            print("Please only enter the integer")
            continue
        if response not in range(1, integer+1):
            print("Please only select from the numbers above.")
            continue
        else:
            break
    return response - 1

def get_team(teams):
    #Return index of team
    print("Here are the teams:")
    display_teams(teams)
    integer = len(teams)
    while True:
        response = input("Please select a number from above: ")
        try:
            response = int(response)
        except ValueError:
            print("Please only enter the integer")
            continue
        if response not in range(1, integer+1):
            print("Please only select from the numbers above.")
            continue
        else:
            break
    return response - 1


def number_players_on_team(team):
    return len(team['roster'])


def num_new_players(team):
    count = 0
    for player in team_players(team, players):
        if player['experience'] == False:
            count += 1
    return count


def num_exp_players(team):
    count = 0
    for player in team_players(team, players):
        if player['experience'] == True:
            count += 1
    return count


def team_players(team, players):
    players_on_team = []
    for player in players:
        if player['name'] in team['roster']:
            players_on_team.append(player)
    return players_on_team


def team_guardians(team, players):
    guardians = set()
    for player in team_players(team, players):
        for guardian in player["guardians"]:
            guardians.add(guardian)
    return list(guardians)


if __name__ == "__main__":
    #setup data
    teams = [{"name" : team, 
              "roster" : []} for team in constants.TEAMS]
    players = clean_data(constants.PLAYERS)
    balance_teams(teams, players)

    #start main loop
    print("\nBasketball Team Stats Tool by SCCroix")
    while True:
        display_menu()
        if get_option_from_user(2) == 0:
            display_team_stats(get_team(teams), teams)
            input("\nPress Enter to Continue...")
        else:
            print("Goodbye")
            break
