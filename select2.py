import streamlit as st
import pandas as pd
st.title("Titanic Clases")

data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(data)
selected_class = st.selectbox("Select Class", data["class"].unique())

st.write(f"Selected Option: {selected_class!r}")
filtered_data_class = data[data["sex"] == selected_class]

st.dataframe(filtered_data_class)