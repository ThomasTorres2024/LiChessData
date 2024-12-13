"""
List of Dependencies
lichess --> pip install python-lichess

"""

from lichess.format import SINGLE_PGN
import lichess.api

def main():
    #user=lichess.api.user("thibault")
    #print(user)

    

    games = lichess.api.user_games('thibault', max=2)
    for game in games:

        #in order to avoid double counting for games we check the hash to see if the game's ID already exists

        print(game['wh'])
        print(game['moves']+"\n")
        
    #with open('last200.pgn', 'w') as f:
    #   f.write(pgn)

    #print(user['perfs'])
    #print(user['blitz'])
    #print(user['rating'])


main()