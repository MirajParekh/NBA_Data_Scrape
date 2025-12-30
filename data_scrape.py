from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.basketball-reference.com/leagues/NBA_stats_per_game.html'
page = requests.get(url)

# cleaning up data to get only the table
soup = BeautifulSoup(page.text, 'html.parser')
col_titles = soup.find_all('tr')[1]
titles = col_titles.find_all('th')
titles_table = [title.text for title in titles]

# insert html data into df
df = pd.DataFrame(columns=titles_table[1:]) #dont need index col 

all_row_data = soup.find('tbody')
rows = all_row_data.find_all('tr')
rows = rows[:20] #since after 20th index, html goes to another table we dont care abt

for row in rows:
    individual_row_stats = row.find_all('td')
    individual_row_stats = [stat.text for stat in individual_row_stats]
    
    length = len(df)
    df.loc[length] = individual_row_stats

df.index = df.get('Season')
df.pop('Season')
    
# print(df.head())
# df_3pt = df.get(['3P', '3PA', '3P%'])

df_3pt = df.get('3P')

# fix problem where cant plot bcus data in the form of str
for i in range(len(df_3pt)):
    df_3pt[i] = float(df_3pt[i])

plot = df_3pt.plot()
plt.show()