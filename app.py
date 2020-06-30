import constants

def convert_height_to_int(str):
    # Convert the text height to an integer
    pass

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
      for key, value in player:
          pass
          # Copy over name
          # Change Guardians to list
          # Change height to an integer
    clean_data.append(clean_player_data)
return clean_data





if __name__ == "__main__":
    print("Basketball Team States Tool by SCCroix\n")
    display_menu()