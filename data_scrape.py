from bs4 import BeautifulSoup
import requests

url = 'https://www.basketball-reference.com/leagues/NBA_stats_per_game.html'
page = requests.get(url)
print(page)