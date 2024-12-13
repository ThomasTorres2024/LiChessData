from lichess.format import SINGLE_PGN
from Game import GameData
import lichess.api
from FileWriter import CSVFileWriter
from LichessWebScraper import LichessScraper

"""Ïterates over a list of players"""
class LichessAPIGameInfo:

    #the file with the best pl;ayers
    player_file_name : str  

    #the output file consisting of all of the games of a player 
    data_file_name : str 

    #number of games we look for  
    iterations_per_account : int 

    #list of top players we will iterate through 
    player_list : list[str]

    #hash of game IDs to Game objects, games should only come up once to reduce redundancy
    game_id_to_game_hash : dict[str,GameData]

    def __init__(self, data_file_name : str, player_file_name : str, iterations_per_account : int):
        self.data_file_name = data_file_name
        self.player_file_name = player_file_name
        self.iterations_per_account = iterations_per_account
        self.player_list = []
        self.game_id_to_game_hash : dict[str,GameData] =  {} 

    """If a file with the expected file name does not exist we create a file at its location"""
    def save_player_list(self):
        #scrape top players and get list of them
        player_scraper : LichessScraper = LichessScraper()
        top_players_set : set = player_scraper.get_top_player_set()

        #save to file
        #print(f"Number of players: {len(top_players_set)}")
        with open(self.player_file_name,'a') as player_out_file:
            for player in top_players_set:
                player_out_file.write(player+"\n")
            player_out_file.close()  
        
        print(f"File for top players created at: {self.player_file_name}")
        
        #set the top player  set
        self.player_list=list(top_players_set)

    """Access the playerlist and get a list of players. In both branches we get our list of players."""
    def gather_data_from_players(self):
        #check if the file for player data exists, if it does not exist, call a function to create player data 
        try:
            with open(self.player_file_name,'r') as player_name_file:
                for line in player_name_file:
                    line.strip()
                    print(line)
                    self.player_list.append(line)

        #if the player  file doesn't exist then create it  
        except FileExistsError or FileNotFoundError as e: 
            print(e)
            print(f"ERROR: Player  file not found at: {self.player_file_name}")
            print(f"Creating file at the given directory: ")
            self.save_player_list()

    """Saves every iteration number of games for each"""
    def save_every_user_game(self):
        
        #initialize the player list 
        self.gather_data_from_players()

        #go through playerlist, get their games,process them, and add them to the list of games 
        for player in self.player_list:
            games = lichess.api.user_games(player, max=self.iterations_per_account)
            i : int = 1
            for game in games:
                id : str = game['id']
                print(f"Player {player} Game {i}")
                try:
                    if id not in self.game_id_to_game_hash:
                        #put game data into game objects, create a hash map where game ID corresponds to game variable 
                        moves : str= game['moves']
                        speed : str = game['speed']
                        white_player : str = game['players']['white']['user']['name']

                        white_elo : int= 0
                        black_elo : int= 0
                        #elo checks 
                        if 'rating' in game['players']['white']:
                            white_elo= game['players']['white']['rating']
                        if 'rating' in game['players']['black']:
                            black_elo= game['players']['white']['rating']

                        black_player : str = game['players']['black']['user']['name']
                        id : str = game['id']

                        #winner is only sometimes included in the dict so i have to do this to get around it
                        result : str = "draw"
                        if 'winner' in game:
                            result  = game['winner']

                        new_game :GameData = GameData(id,white_player,black_player,int(white_elo),int(black_elo),result,moves,speed)
                        self.game_id_to_game_hash[id] = new_game
                        i+=1
                except Exception as e:
                    print(e)
        #save file 
        csv_writer : CSVFileWriter = CSVFileWriter(self.game_id_to_game_hash.values(),self.data_file_name)
        csv_writer.write_to_dir()