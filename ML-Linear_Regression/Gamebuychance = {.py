Gamebuychance = {
    'Game_Name' : ['COD' , 'Minecraft' , 'Genshin_impact'],
    'Price' : [2 , 1 ,5],
    'Buy' : ['yes' ,'no' , 'no']
}

import pandas as pd
import matplotlib as plt

df = pd.DataFrame(Gamebuychance)
df.to_csv('Will_they_buy?..csv', index = False)
