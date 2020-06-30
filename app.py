import constants
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

def convert_height_to_int(str):
    # Convert the text height to an integer
    return int(str.split()[0])

def convert_exp_to_bool(str):
    # Converts 'YES' or 'NO' to true false
    return str == "YES"
    

def display_menu():
    print("\n ____ Menu ____ \n")
    print("""
Here are your choices:
  1) Display Team Stats
  2) Quit
""")

def clean_player_data(players):
    clean_data = []
    #iterate through the list of players
    for player in players:
        # for each player iterate through key value pairs
        clean_player_data = {}
        # Copy over name
        clean_player_data['name'] = player['name']
        # Change Guardians to list
        # Change height to an integer
        clean_player_data['height'] = convert_height_to_int(player['height'])
        # Change experienced to true false
        clean_player_data['experience'] = convert_exp_to_bool(player['experience'])
        clean_data.append(clean_player_data)
    logging.debug(clean_data)
    return clean_data

clean_player_data(constants.PLAYERS)

if __name__ == "__main__":
    print("Basketball Team States Tool by SCCroix\n")
    display_menu()