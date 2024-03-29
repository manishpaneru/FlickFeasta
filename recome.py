# -*- coding: utf-8 -*-
"""Recome

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15uvrMdnw_k6gyakAEPvh2FB0SGeksV15
"""

import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
from sklearn.metrics.pairwise import cosine_similarity
import pickle

credits = pd.read_csv('tmdb_5000_credits.csv')
movies = pd.read_csv('tmdb_5000_movies.csv')

credits.head(2)
credits.shape
movies = movies.merge(credits, on='title')

# Columns to keep: genres, keywords, cast, crew, overview, title, movie_id
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.isnull().sum()
movies.dropna(inplace=True)
movies.duplicated().sum()

def convert(obj):
    l = []
    for i in ast.literal_eval(obj):
      l.append(i['name'])
    return l

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

def convert2(obj):
    l = []
    counter = 0
    for i in ast.literal_eval(obj):
      if counter != 3:
        l.append(i['name'])
        counter += 1
      else:
        break
    return l

movies['cast'] = movies['cast'].apply(convert2)

def convert3(obj):
    l = []
    for i in ast.literal_eval(obj):
      if i['job'] == 'Director':
          l.append(i['name'])
          break
    return l

movies['crew'] = movies['crew'].apply(convert3)

movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['crew'] = movies['crew'].apply(lambda x: [i.replace(" ", "") for i in x])

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

movies_new = movies[['movie_id', 'title', 'tags']]
movies_new['tags'] = movies_new['tags'].apply(lambda x: " ".join(x))
movies_new['tags'] = movies_new['tags'].apply(lambda x: x.lower())

def stem(text):
  y = []
  for i in text.split():
      y.append(ps.stem(i))
  return " ".join(y)

movies_new['tags'] = movies_new['tags'].apply(stem)
vectors = cv.fit_transform(movies_new['tags']).toarray()

similarity = cosine_similarity(vectors)

def recommend(movie):
    movie_index = movies_new[movies_new['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        print(movies_new.iloc[i[0]].title)

recommend('Avatar')

pickle.dump(movies_new, open('movies.pkl' , 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))
