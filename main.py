"""
List of Dependencies
lichess --> pip install python-lichess

"""

from lichess.format import SINGLE_PGN
from Game import GameData
import lichess.api
from FileWriter import CSVFileWriter
from LichessWebScraper import LichessScraper 
from LiChessAPIGameInfoObtainer import LichessAPIGameInfo

def new_f():
    player_scraper : LichessScraper = LichessScraper()
    top_players_set : set = player_scraper.get_top_player_set()
    print(f"Number of players: {len(top_players_set)}")
    player_file_name = "PlayerData/test.csv"
    with open(player_file_name,'w') as player_out_file:
        for player  in top_players_set:
            player_out_file.write(player+"\n")
        player_out_file.close()  

def main():
    #user=lichess.api.user("thibault")
    #print(user)
    OUT_DIR : str = "GameData/test.csv"
    PLAYER_DATA_DIR : str = "PlayerData/test.csv"
    testSaver : LichessAPIGameInfo  = LichessAPIGameInfo(OUT_DIR,PLAYER_DATA_DIR,1000)
    testSaver.save_every_user_game()

    #with open('last200.pgn', 'w') as f:
    #   f.write(pgn)

    #print(user['perfs'])
    #print(user['blitz'])
    #print(user['rating'])


main()