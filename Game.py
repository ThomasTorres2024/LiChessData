"""Data object representing a game, with its outcomes, players, players elos, and the ID of the game so the game can be looked up again,
if necessary."""
class GameData:

    #every game has a unique id, its url can be accessed with this ID 
    game_id : str 
    white_elo : int 
    black_elo : int

    #outcome 
    outcome : str
    move_string : str  
    speed : str

    """Create game init everything"""
    def __init__(self, game_id : str, white_id : str, black_id : str, white_elo : int, black_elo :int, outcome : str, move_string : str, speed : str):
        self.game_id=game_id
        self.white_elo=white_elo
        self.white_id=white_id
        self.black_id=black_id
        self.black_elo=black_elo
        self.outcome=outcome
        self.move_string=move_string
        self.speed=speed

    #Getters and setter for game speed type 
    def set_speed(self, new_speed : int):
        self.speed=new_speed

    def get_speed(self):
        return self.speed

    # Getter and setter for game_id
    def get_game_id(self):
        return self.game_id

    def set_game_id(self, game_id):
        self.game_id = game_id

    # Getter and setter for white_elo
    def get_white_elo(self):
        return self.white_elo

    def set_white_elo(self, white_elo):
        self.white_elo = white_elo

    # Getter and setter for black_elo
    def get_black_elo(self):
        return self.black_elo

    def set_black_elo(self, black_elo):
        self.black_elo = black_elo

    # Getter and setter for outcome
    def get_outcome(self):
        return self.outcome

    def set_outcome(self, outcome):
        self.outcome = outcome

    # Getter and setter for move_string
    def get_move_string(self):
        return self.move_string

    def set_move_string(self, move_string):
        self.move_string = move_string

        # Getter and setter for white_id
    def get_white_id(self):
        return self.white_id

    def set_white_id(self, white_id):
        self.white_id = white_id

    # Getter and setter for black_id
    def get_black_id(self):
        return self.black_id

    def set_black_id(self, black_id):
        self.black_id = black_id
    
    #Other Methods 
    """Object status"""
    def __str__(self):
        out : str = f"""Game ID: {self.game_id} White ID: {self.white_id} Black ID: {self.black_id}\nWhite Elo:{self.white_elo}\nBlack Elo:{self.black_elo}
        \nspeed:{self.speed} Outcome: {self.outcome}
        \nMoves:{self.move_string}"""

        return out 
    
    """Returns game object data as a line of a csv file, includes the new line character as well"""
    def get_data_as_csv_line(self):
        return  f"{self.game_id},{self.white_elo},{self.black_elo},{self.white_id},{self.black_id},{self.outcome},{self.move_string},{self.speed}\n"
         