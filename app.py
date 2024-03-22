import streamlit as st
import pickle
import pandas as pd



def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    
    recommend_movies = []
    for i in distances[1:6]:
        movie_id = i[0]
        #we have to fetch poster from api
        
        recommend_movies.append(movies_list.iloc[i[0]].title)
    return recommend_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_lst = movies_list['title'].values
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select your movie',
    movies_lst
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    for i in recommendations:
        st.write(i)