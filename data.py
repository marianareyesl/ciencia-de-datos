import pandas as pd
import streamlit as st

names_link = "https://raw.githubusercontent.com/marianareyesl/generos-de-musica/refs/heads/main/music_genre.csv"

names_data = pd.read_csv(names_link)