import streamlit as st
import pickle
# import numpy as np
# import pandas as pd
import requests

#TMDB
def fetch_poster(movie_id):
    api_key='c4fe22ade6332f709d42fe7e655c1f6c'
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,api_key))
    data=response.json()
    # st.text(data)
    # st.text('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,api_key))
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    

def recommend(movie):
    movie_index=movies_lst[movies_lst['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    recommended_movies_poster=[]
    
    for i in movies_list:
        movie_id=movies_lst.iloc[i[0]].movie_id
        recommended_movies.append((movies_lst.iloc[i[0]].title))
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
        #print(movies_lst.iloc[i[0]].title)   
    return recommended_movies,recommended_movies_poster

movies_lst=pickle.load(open('movies.pkl','rb'))
#movies_lst=movies_lst['title'].values
movie_titles = movies_lst['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
# pip install streamlit =>(command to run) python -m streamlit run rec.py

selected_movie = st.selectbox(
    "How would you like to be contacted?",
    (movie_titles)
)

    
if st.button("Recommendation"):
    names,posters=recommend(selected_movie)
    # for i in recommended:
    #     st.write(i)
    col1, col2, col3 ,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
#st.write("You selected:", option)

