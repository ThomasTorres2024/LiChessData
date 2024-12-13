from bs4 import BeautifulSoup
import requests

""""Scrapes LiChess Leaderboards for bullets, blitz, rapid, and classical, and gets a set of the top
players in each area"""
class LichessScraper:

    """Creates scraper for the usernames and then scrapes them from the site"""
    def __init__(self):
        self.leaderboard_root = "https://lichess.org/player/top/200/"
        self.top_players= set()
        site_types  : list[str] = ["bullet","blitz","rapid","classical"]
        self.scrape_given_type(site_types)

    """Outputs site info into the set of usernames in the leaderboard."""
    def parse_top_200_leaderboard(self, site_souped_info : BeautifulSoup) -> None:

        #look for links of online and offline users in the top 200 and add them to the set of top players 
        online_a = site_souped_info.find_all("a",{"class":"online"})
        offline_a = site_souped_info.find_all("a",{"class":"offline"})
        for online_user in online_a:
            print(online_user)
            print(online_user.get("href")[3:])
            self.top_players.add(online_user.get("href")[3:])
        for offline_user in offline_a:
            print(offline_user)
            print(offline_user.get("href")[3:])
            self.top_players.add(offline_user.get("href")[3:])


    """Scrapes a given site putting every name found into a list of names"""
    def scrape_given_type(self, sites : list[str]) -> None:
        for site in sites:
            site_link : str = f"{self.leaderboard_root}{site}"

            #try to access the site get data, feed to smaller function to parse the HTML of the site 
            try: 
                site_raw_request_data  = requests.get(site_link)
                site_raw_request_data.raise_for_status()
                souped_site_data : BeautifulSoup = BeautifulSoup(site_raw_request_data.text)
                self.parse_top_200_leaderboard(souped_site_data)
            #if site DNE 
            except  requests.exceptions.HTTPError as err:
                print(f"ERROR. The domain: {site_link} is an invalid link, and could not be accessed.")
                print(err)
            

    """Returns the top players as a set"""
    def get_top_player_set(self) -> set:
        return self.top_players
    
    """Sets top player set"""
    def set_top_player_set(self, new_top_players :set) -> None:
        self.top_players=new_top_players
