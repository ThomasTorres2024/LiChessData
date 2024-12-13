from dataclasses import dataclass

@dataclass
class Game:

    #every game has a unique id, its url can be accessed with this ID 
    game_id : str 
    white_elo : int 
    black_elo : int

    #outcome 
    #0--> white wins
    #1--> black wins
    #2--> draw 
    outcome : int
    move_string : str  

    #for this project I only want to use certain game types so i will have a way to encode these because
    #string comparisons are cumbersome (tbf using this kind of encoding im afraid just makes things unnecessarily complex with)
    #marginal benefits but u tell me what u think.
    #
    #0--> correspondence, 1-->classical, 2-->rapid, 3-->blitz, 4-->bullet, can add more in the future, this is it fn  
    variant : int

    """Create game init everything"""
    def __init__(self, game_id : str, white_id : str, black_id : str, white_elo : int, black_elo :int, outcome : int, move_string : str, variant : int):
        self.game_id=game_id
        self.white_elo=white_elo
        self.white_id=white_id
        self.black_id=black_id
        self.black_elo=black_elo
        self.outcome=outcome
        self.move_string=move_string
        self.variant=variant

    #Getters and setter for game variant type 
    def set_variant(self, new_variant : int):
        self.variant=new_variant

    def get_variant(self):
        return self.variant

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
        \nVariant:{self.variant}\nOutcome as Num: {self.outcome} Outcome: {self.output_state()}
        \nMoves:{self.move_string}"""
    
    """Writes info to a CSV file"""
    def write_to_file(self,dir : str):
        pass 

    """Returns the output state in plain text"""
    def output_state(self):
        match self.variant:
            case 0:
                return"white wins"
            case 1:
                return "black wins"
            case 2:
                return "draw"  