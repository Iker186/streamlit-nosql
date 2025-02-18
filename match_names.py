import streamlit as st
import pandas as pd

DATA_URL = "dataset.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

def search_matches(name, df):
    if name:
        return df[df['name'].str.contains(name, case=False, na=False)]

st.title("Search Names in Dataset")

st.write('Iker Gerardo Guevara Sanchez')
st.write('zs22004366')
st.image("foto.jpeg")

df = load_data()

myname = st.text_input("Enter a name:")

if myname:
    results = search_matches(myname, df)
    st.write(f"### Found {len(results)} matches:")
    st.dataframe(results)
else:
    st.info("Please enter a name to search.")
