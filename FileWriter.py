from Game import GameData

"""Class that outputs a text file of games played in the form of a CSV file"""
class CSVFileWriter:

    #the list of games we  are  writing
    game_data_list : list[GameData]
    #default header at the top of the csv 
    header : str 

    """Creates CSV writer and writes objects to CSV file"""
    def __init__(self, game_data_list : list[GameData], directory : str):
        #initialize all vals then write to file 
        self.game_data_list= game_data_list  
        self.dir = directory
        self.header = "Game ID,White Elo, Black Elo,White ID,Black ID,Outcome,Move String,Speed\n"


    """Writes file to given directory"""
    def write_to_dir(self):
        #open file in write mode
        with open(self.dir, 'w') as datafile:

            #write header part 
            datafile.write(self.header)
            for game in self.game_data_list: 
                datafile.write(game.get_data_as_csv_line())

            datafile.close()
        
        print(f"File successfully saved to: {self.dir}")