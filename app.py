import streamlit as st
import requests
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to fetch poster URL
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to calculate similarity dynamically
def calculate_similarity(movies):
    tags = movies['tags']
    vectors = cv.fit_transform(tags).toarray()
    return cosine_similarity(vectors)

# Function to recommend movies
def recommend(movie, movies):
    index = movies[movies['title'] == movie].index[0]
    similarity = calculate_similarity(movies)
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        poster_path = fetch_poster(movie_id)
        recommended_movies.append({'title': movies.iloc[i[0]].title, 'poster_path': poster_path})
    return recommended_movies

# Set background color to white
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header('FlickFeasta')
st.write("by Manish Paneru")  # Added aesthetic change

# Load pickled files
movies = pd.read_pickle('movie_list.pkl')

# Initialize CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

# Add more vertical spacing
st.write("\n\n\n\n\n")  

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Please enter a movie name",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movies = recommend(selected_movie, movies)
    cols = st.columns(5)
    for i, movie in enumerate(recommended_movies):
        with cols[i]:
            st.image(movie['poster_path'], width=100)
            st.markdown(f"**{movie['title']}**")
        st.write("")  # Add some space between columns
