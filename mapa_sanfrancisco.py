import pandas as pd
import numpy as np
import streamlit as st

map_data = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])

st.title("San francisco Map")
st.header("Using Streamlit and Mapbox")

st.map(map_data)

sidebar = st.sidebar

sidebar.title("barra lateral")

sidebar.write("Aqui van los elementos de entrada.")
sidebar.write('Iker Gerardo Guevara Sanchez')
sidebar.write('zs22004366@estudiantes.uv.mx')
sidebar.image("credencial.jpeg")