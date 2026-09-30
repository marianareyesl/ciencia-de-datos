import streamlit as st
import datetime

#Dar al usuario la fecha actual
today = detetime.date.today()
today_date = st.date_input("Current date", today)
st.succes("Current date: %s")