# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import dataset
cr_df = pd.read_csv('titles.csv')

# drop table
a = cr_df.drop(['id', 'type', 'description', 'production_countries', 'imdb_id', 'imdb_votes', 'release_year', 'age_certification', 'genres', 'runtime', 'seasons', 'tmdb_popularity', 'tmdb_score'], axis = 1)

# argument, exclude null, sort values
a[cr_df['imdb_score']>8.8].groupby(['title', 'imdb_score']).max()
a.dropna(subset=['imdb_score'], inplace=True)
a.sort_values(by=['imdb_score'], ascending=False)

a.plot()

# drop table, exclude null, sort values
b = cr_df.drop(['id', 'type', 'title', 'release_year', 'description', 'production_countries', 'imdb_score', 'imdb_votes', 'tmdb_popularity', 'tmdb_score', 'imdb_id'], axis = 1)
b.dropna(subset=['age_certification', 'seasons'], inplace=True)
b.sort_values(by=['seasons', 'runtime'], ascending=False)

# print mean of runtime & seasons
print(b['runtime'].mean())
print(b['seasons'].mean())

b.plot()
