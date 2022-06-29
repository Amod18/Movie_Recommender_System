from ctypes import cast
import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image

img = Image.open('fav.png')
st.set_page_config(page_title='Movie Recommender', page_icon=img)

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similar = pickle.load(open('similar.pkl', 'rb'))


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=afa0f12c4f651b1408edcc2de85958ad&language=en-US'.format(movie_id))
    data = response.json()
    if(data['poster_path'] == None):
        return "data:image/png;base64,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"
    return "https://image.tmdb.org/t/p/original"+data['poster_path']


def fetch_date(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=afa0f12c4f651b1408edcc2de85958ad&language=en-US'.format(movie_id))
    data = response.json()
    return data['release_date']


def fetch_genre(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=afa0f12c4f651b1408edcc2de85958ad&language=en-US'.format(movie_id))
    data = response.json()
    object = data['genres']
    res = ""
    for obj in object:
        res = res+obj['name']+", "
    res = res.rstrip(res[-1])
    res = res.rstrip(res[-1])
    return res


def fetch_vote(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=afa0f12c4f651b1408edcc2de85958ad&language=en-US'.format(movie_id))
    data = response.json()
    return data['vote_average']


def fetch_cast(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}/credits?api_key=afa0f12c4f651b1408edcc2de85958ad&language=en-US'.format(movie_id))
    data = response.json()
    object = data['cast']
    res = ""
    count = 0
    for obj in object:
        if (count == 4):
            break
        res = res + obj['name'] + ", "
        count += 1
    res = res.rstrip(res[-1])
    res = res.rstrip(res[-1])
    return res


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similar[movie_index]
    movies_lst = sorted(list(enumerate(distances)),
                        reverse=True, key=lambda x: x[1])[0:6]
    recommended_movies = []
    recommended_movies_poster = []
    recommended_movies_date = []
    recommended_movies_genres = []
    recommended_movies_vote = []
    recommended_movie_cast = []
    for i in movies_lst:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append((movies.iloc[i[0]].title))
        # Fetching the movie poster
        recommended_movies_poster.append(fetch_poster(movie_id))
        #
        recommended_movies_date.append(fetch_date(movie_id))
        #
        recommended_movies_genres.append(fetch_genre(movie_id))
        #
        recommended_movies_vote.append(fetch_vote(movie_id))
        #
        recommended_movie_cast.append(fetch_cast(movie_id))

    return recommended_movies, recommended_movies_poster, recommended_movies_date, recommended_movies_vote, recommended_movies_genres, recommended_movie_cast


st.title('Movies Recommender')
selected_movie = st.selectbox(
    'On which movies would you like to have recommendations',
    (movies['title'].values))

if st.button('Recommed :-)'):
    names, poster, date, votes, genres, cast = recommend(selected_movie)

    st.subheader("Selected Movie")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        with st.container():
            st.subheader(names[0])
            st.image(poster[0], width=250)
            st.write("**Movie Cast** - " + str(cast[0]))
            st.write("**Release Date** - " + date[0])
            st.write(":star: " + ": " + str(votes[0]))

            with st.expander("Genres"):
                st.write(genres[0])

    with col3:
        st.write("")

    st.subheader('Recommended Movies')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(poster[1])
        st.text(names[1])
        st.write("**Movie Cast** - " + str(cast[1]))
        st.write("**Release Date:** " + date[1])
        st.text("⭐" + ": " + str(votes[1]))
        with st.expander("Genres"):
            st.write(genres[1])
    with col2:
        st.image(poster[2])
        st.text(names[2])
        st.write("**Movie Cast** - " + str(cast[2]))
        st.write("**Release Date:** " + date[2])
        st.text("⭐" + ": " + str(votes[2]))
        with st.expander("Genres"):
            st.write(genres[2])
    with col3:
        st.image(poster[3])
        st.text(names[3])
        st.write("**Movie Cast** - " + str(cast[3]))
        st.write("**Release Date:** " + date[3])
        st.text("⭐" + ": " + str(votes[3]))
        with st.expander("Genres"):
            st.write(genres[3])
    
    col4, col5 = st.columns(2)
    with col4:
        st.image(poster[4])
        st.text(names[4])
        st.write("**Movie Cast** - " + str(cast[4]))
        st.write("**Release Date:** " + date[4])
        st.text("⭐" + ": " + str(votes[4]))
        with st.expander("Genres"):
            st.write(genres[4])
    with col5:
        st.image(poster[5])
        st.text(names[5])
        st.write("**Movie Cast** - " + str(cast[5]))
        st.write("**Release Date:** " + date[5])
        st.text("⭐" + ": " + str(votes[5]))
        with st.expander("Genres"):
            st.write(genres[5])


st.write(':copyright: 2022 movie_recommendations_AN18')
