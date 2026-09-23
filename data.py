import streamlit as st
import pandas as pd

names_link = "https://raw.githubusercontent.com/marianareyesl/generos-de-musica/refs/heads/main/music_genre.csv"
names_data = pd.read_csv(names_link)

st.title("streamlit and pandas")
st.data(names_data)