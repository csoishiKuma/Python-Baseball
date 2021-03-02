import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']
# print(plays)
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)')]
hits = hits[['inning', 'event']]
hits['inning'] = pd.to_numeric(hits.loc[:, 'inning'])
# print(hits)
replacements = {
    "r'^S(.*)'": 'single',
    "r'^D(.*)'": 'double',
    "r'^T(.*)'": 'triple',
    "r'^HR(.*)'": 'hr'
}

hit_type = hits[hits['event']].replace(replacements, regex=True)
print(hit_type)