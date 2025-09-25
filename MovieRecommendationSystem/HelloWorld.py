import numpy as np
import pandas as pd

movies = pd.read_csv('./MovieRecommendationSystem/corpus/tmdb_5000_movies.csv', encoding='latin-1')
credits = pd.read_csv('./MovieRecommendationSystem/corpus/tmdb_5000_credits.csv', encoding='latin-1')
#print("Hello World!")
print(movies.head(1))
#print(credits.head())