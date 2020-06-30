import constants
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

def balance_teams(teams, players):
    """ Distributes players to teams """



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
    print("\n ____ Menu ____ \n")
    print("""
Here are your choices:
  1) Display Team Stats
  2) Quit
""")


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
    logging.debug(clean_player_data)
    return clean_player_data


if __name__ == "__main__":
    teams = constants.TEAMS
    players = clean_data(constants.PLAYERS)
    print("Basketball Team States Tool by SCCroix\n")
    display_menu()