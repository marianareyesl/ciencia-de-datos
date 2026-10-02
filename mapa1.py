import pandas as pd
import numpy as np 
import streamlit as st

map_data = pd.DataFrame(
np.random.randn(100, 2) / [50, 50] + [18.91534, -97.02848],
columns=['lat', 'lon'])

st.map(map_data)