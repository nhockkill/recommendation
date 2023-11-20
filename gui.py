import streamlit as st
import pickle

# import pandas as pd
# import numpy as np
# from sklearn.feature_extraction.text import CountVectorizer    
# from sklearn.metrics.pairwise import cosine_similarity

import data_processing
from data_processing import clean_data


#read data
movies = pickle.load(open("movies_list.pkl", 'rb'))
# print(movies)ruu
similarity = pickle.load(open("similarity.pkl", 'rb'))
# print(similarity)
movies_list = movies['Title'].values

 
st.header("Movie Recommendation System")
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies['Title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse= True, key=lambda vector:vector[1])
    recommend_movie = []
    for i in distance [1:6]:
        recommend_movie.append(movies.iloc[i[0]].Title)
    return recommend_movie


if st.button("Show Recommend"):
    movie_name = recommend(selectvalue)
    col1, col2, col3, col4, col5 =st.columns(5)
    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:    
        st.text(movie_name[4])
 