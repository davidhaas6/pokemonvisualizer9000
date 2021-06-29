
#%%
import pandas as pd
from chord import Chord
#%%
df = pd.read_csv('pokemon_cleaned.csv')
df['type_1'] = df.type_1.astype('category')
df['type_2'] = df.type_2.astype('category')

# %%
types = pd.concat([df.type_1.cat.codes, df.type_2.cat.codes],axis=1)
types = types.rename(columns={0:'type1',1:'type2'})
categories = df.type_1.cat.categories.to_list()  # pokepeople type names

types = types[~types.type2.isna()]  # drop nans yall

# Create a co-occurrence matrix
mtx = pd.crosstab(types.type1, types.type2).to_numpy()  # co-occurrence matrix
# %%
pokeman_colors = [
    '#1C4B27', '#040706', '#438B95', '#E3E32B', '#971944', '#994025',
    '#AB1F23', '#4A677D', '#333369', '#147B3D', '#A9702C', '#86D2F5',
    '#75515B', '#5C2D89', '#A42A6C', '#48180B', '#5F756D', '#1552E2'
]
Chord(mtx.tolist(), categories, padding=1, colors=pokeman_colors).to_html()
# %%
