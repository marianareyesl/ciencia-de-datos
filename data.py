import pandas as pd
import streamlit as st

names_link = "https://raw.githubusercontent.com/marianareyesl/generos-de-musica/refs/heads/main/music_genre.csv"
names_dataframe = pd.read_csv(names_link)

st.title ("streamlit and pandas")
st.dataframe(names_data)