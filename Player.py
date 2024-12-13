"""Dataclass representing a player where ever player has a unique UID and a list of games assosciated with their account"""
class Player:
    id : str
    user : str
    blitz_info:dict[str,int]
    rapid_info:dict[str,int]
    correspondence_info:dict[str,int]
    classical:dict[str,int]
    def __init__(self,user_info:dict[dict[str,int]]):
        self.id=user_info['id']
        self.user=user_info['username']

        rating_info : dict[dict[str,int]] = user_info['perfs']


        pass 

    def write_to_file(self,file_name : str):
        pass 

    #Getters
    def get_uid(self):
        pass 
        
    """Gets the"""
    def get_game_list(self):
        pass 

    #Setters 
    def set_game_list(self):
        pass 

    """Sets UID to a new UID"""
    def set_uid(self, new_uid):
        self.uid = new_uid