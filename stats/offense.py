import pandas as pd
import matplotlib.pyplot as plt
from data import games

plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']
plays = plays[plays.loc[:,'event'].str.contains('^(?:S(?!B)|D|T|HR)')]
hits = plays[['inning', 'event']]
hits.loc[:, ['inning']].apply(pd.to_numeric)

replacements = {
    "r'^S(.*)'": 'single',
    "r'^D(.*)'": 'double',
    "r'^T(.*)'": 'triple',
    "r'^HR(.*)'": 'hr'
}
hit_type = hits[hits['event']].replace(replacements, regex=True)
