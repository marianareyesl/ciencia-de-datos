import streamlit as st
import pandas as pd 
st.title("hola")
dataframe = pd.read_csv("https://raw.githubusercontent.com/marianareyesl/generos-de-musica/refs/heads/main/music_genre.csv")
st.dataframe(dataframe)
st.write("by marianareyesl")
