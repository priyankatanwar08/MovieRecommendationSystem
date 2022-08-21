#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import warnings 
#%%
data = pd.read_csv('movie_metadata.csv')
#%%
data.head(5)
# %%
print(data.shape)
data.columns

# %%
data.title_year.value_counts(dropna=False).sort_index().plot(kind='barh',figsize=(15,16))

# %%
#for recommendation based on certain features 
#consider all rows and columns with these specific headings
data=data.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres','movie_title']]
data['genres']=data['genres'].str.replace('|',' ')
data['movie_title']=data['movie_title'].str.lower()
data.head(10)
# %%
data['comb'] = data['actor_1_name'] + ' ' + data['actor_2_name'] + ' '+ data['actor_3_name'] + ' '+ data['director_name'] +' ' + data['genres']

# %%
data['movie_title'][1]
# %%
data['movie_title'] = data['movie_title'].apply(lambda x : x[:-1])
data['movie_title'][1]

# %%
data.to_csv('data.csv',index=False)
# %%
credits = pd.read_csv('credits.csv')
# %%
meta = pd.read_csv('movies_metadata.csv')
# %%
meta['release_date'] = pd.to_datetime(meta['release_date'], errors='coerce')
meta['year'] = meta['release_date'].dt.year
meta['year'].value_counts().sort_index()
meta['year'].value_counts(dropna=False).sort_index().plot(kind='barh',figsize=(20,50))
# %%
meta = meta.loc[meta.year == 2017,['genres','id','title','year']]

# %%
meta['id'] = meta['id'].astype(int)
data_1 = pd.merge(meta, credits, on='id')
data_1
# %%
import ast
data_1['genres'] = data_1['genres'].map(lambda x: ast.literal_eval(x))
data_1['cast'] = data_1['cast'].map(lambda x: ast.literal_eval(x))
data_1['crew'] = data_1['crew'].map(lambda x: ast.literal_eval(x))
# %%
def genresList(x):
    genre = []
    st = " "
    for i in x:
        if i.get('name') == 'Science Fiction':
            genre.append('Sci-Fi')
        else:
            genre.append(i.get('name'))
    if genre == []:
        return np.NaN
    else:
        return (st.join(genre))
data_1['genres_list'] = data_1['genres'].map(lambda x: genresList(x))
data_1['genres_list']
# %%
def get_actor1(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == []:
        return np.NaN
    else:
        return (casts[0])
data_1['actor_1_name'] = data_1['cast'].map(lambda x: get_actor1(x))
data_1['actor_1_name']
# %%
def get_actor2(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == [] or len(casts)<=1:
        return np.NaN
    else:
        return (casts[1])
data_1['actor_2_name'] = data_1['cast'].map(lambda x: get_actor2(x))
data_1['actor_2_name']
# %%
def get_actor3(x):
    casts = []
    for i in x:
        casts.append(i.get('name'))
    if casts == [] or len(casts)<=2:
        return np.NaN
    else:
        return (casts[2])
data_1['actor_3_name'] = data_1['cast'].map(lambda x: get_actor3(x))
data_1['actor_3_name']
# %%
def get_directors(x):
    dt = []
    st = " "
    for i in x:
        if i.get('job') == 'Director':
            dt.append(i.get('name'))
    if dt == []:
        return np.NaN
    else:
        return (st.join(dt))
data_1['director_name'] = data_1['crew'].map(lambda x: get_directors(x))
data_1['director_name']
# %%
movie = data_1.loc[:,['director_name','actor_1_name','actor_2_name','actor_3_name','genres_list','title']]
movie
# %%
movie.isna().sum()
# %%
movie = movie.dropna(how='any')
movie.isna().sum()
# %%
movie = movie.rename(columns={'genres_list':'genres'})
movie = movie.rename(columns={'title':'movie_title'})
movie['movie_title'] = movie['movie_title'].str.lower()
movie['comb'] = movie['actor_1_name'] + ' ' + movie['actor_2_name'] + ' '+ movie['actor_3_name'] + ' '+ movie['director_name'] +' ' + movie['genres']
movie
# %%
new_data=data.append(movie)
new_data
# %%
new_data.drop_duplicates(subset ="movie_title", keep = 'last', inplace = True)
new_data
# %%
new_data.to_csv('new_data.csv',index=False)
# %%


