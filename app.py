import streamlit as st
import pickle
import difflib

# Page config
st.set_page_config(page_title="Movie Recommender", layout="centered")

# CSS styling
st.markdown("""
<style>

.stApp {
    background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Title */
h1 {
    text-align: center;
    color: #00ffd5;
    white-space: nowrap;
}

/* Button */
div.stButton > button {
    background-color: #00ffd5;
    color: black;
    border-radius: 6px;
    height: 40px;
    width: 180px;
    font-size: 15px;
    font-weight: bold;
}

/* Disable hover color change */
div.stButton > button:hover {
    background-color: #00ffd5;
    color: black;
}

/* Black box for recommendations */
.rec-box {
    background-color: rgba(0,0,0,0.85);
    padding: 15px;
    border-radius: 8px;
    margin-top: 10px;
}

/* Movie list */
.movie {
    color: white;
    font-size: 17px;
    margin: 3px 0;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🎬 Movie Recommendation System")

# Load data
movies_data = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Input
movie_name = st.text_input("Enter movie name")

# Recommendation function
def recommend(movie):

    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie, list_of_all_titles)

    if len(find_close_match) == 0:
        return []

    close_match = find_close_match[0]

    index_of_movie = movies_data[movies_data.title == close_match].index.values[0]

    similarity_score = list(enumerate(similarity[index_of_movie]))

    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []

    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]

        if i <= 10:
            recommended_movies.append(title_from_index)
            i += 1

    return recommended_movies


# Button
if st.button("Recommend"):

    movies = recommend(movie_name)

    if len(movies) == 0:
        st.warning("Movie not found. Try another name.")

    else:

        html = '<div class="rec-box">'

        for i, movie in enumerate(movies, 1):
            html += f'<div class="movie">{i}. {movie}</div>'

        html += "</div>"

        st.markdown(html, unsafe_allow_html=True)