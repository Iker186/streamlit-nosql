import streamlit as st
import pandas as pd

DATA_URL = "dataset.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    df = df.reset_index()  
    return df

def search_by_index(index, df):
    if index.isdigit():  
        index = int(index)
        if index in df.index:
            return df.loc[[index]]
    return pd.DataFrame() 

def search_by_range(start, end, df):
    if start.isdigit() and end.isdigit():
        start, end = int(start), int(end)
        return df.iloc[start:end+1]  
    return pd.DataFrame()

df = load_data()

st.title("Search in Database")

st.write('Iker Gerardo Guevara Sanchez')
st.write('zs22004366')
st.image("foto.jpeg")

st.subheader("Search by Index")
index_search = st.text_input("Enter an index:")
if st.button("Search Name by Index"):
    result = search_by_index(index_search, df)
    if not result.empty:
        st.write("### Match Found:")
        st.dataframe(result)
    else:
        st.warning("No match found for this index.")

st.subheader("Search by Range of Indexes")
start_index = st.text_input("Start Index:")
end_index = st.text_input("End Index:")

if st.button("Search Names in Range"):
    range_results = search_by_range(start_index, end_index, df)
    if not range_results.empty:
        st.write(f"### Found {len(range_results)} matches:")
        st.dataframe(range_results)
    else:
        st.warning("No matches found in this range.")
