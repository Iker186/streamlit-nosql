import streamlit as st
import pandas as pd

DATA_URL = "dataset.csv"
LENGTH_DATA = sum(1 for _ in open(DATA_URL)) - 1 

@st.cache_data
def load_data(nrows):
    return pd.read_csv(DATA_URL, nrows=nrows)

st.title("Cache Example")

st.write('Iker Gerardo Guevara Sanchez')
st.write('zs22004366')
st.image("foto.jpeg")

nrows = st.number_input("Number of rows to load", 1, LENGTH_DATA)

df = load_data(nrows)

st.dataframe(df)
