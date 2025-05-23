import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv('movies.csv')

#movies_data.shape
#print(movies_data)
selected_features = ['keywords', 'genres', 'tagline', 'cast', 'director']
#print(selected_features)

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data['genres']+' '+movies_data['keywords']+' ' +movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
#print(combined_features)
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
#print(feature_vectors)

similarity = cosine_similarity(feature_vectors)
#print(similarity)

movie_name = input("Enter your favourite movie name: ")

list_of_all_titles = movies_data['title'].tolist()
#print(list_of_all_titles)

find_the_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
#print(find_the_close_match)

close_match = find_the_close_match[0]
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
#print(index_of_the_movie)

similarity_score = list(enumerate(similarity[index_of_the_movie]))
#print(similarity_score)

len(similarity_score)
sorted_movies = sorted(similarity_score, key = lambda x:x[1], reverse=True)
#print(sorted_movies)

print('Movies suggested for you: \n')

i=1
for movie in sorted_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if i<30:
        print(i, '.', title_from_index)
        i += 1
