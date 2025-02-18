import streamlit as st
import pandas as pd

DATA_URL = "dataset.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_URL)

def filter_by_sex(sex, df):
    return df[df["sex"] == sex]

df = load_data()

st.title("Filter by Gender")

st.write('Iker Gerardo Guevara Sanchez')
st.write('zs22004366')
st.image("foto.jpeg")

selected_sex = st.selectbox("Select Gender:", ["F", "M"])

if st.button("Filter"):
    filtered_df = filter_by_sex(selected_sex, df)
    count = len(filtered_df)

    st.write(f"### Found {count} {'women' if selected_sex == 'F' else 'men'} in the dataset.")
    st.dataframe(filtered_df)
