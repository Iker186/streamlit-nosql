import streamlit as st
import pandas as pd

DATA_URL = "dataset.csv"

@st.cache_data
def load_data(nrows=None):
    return pd.read_csv(DATA_URL, nrows=nrows)

def search_matches(name, df):
    if name:
        return df[df['name'].str.contains(name, case=False, na=False)]
    return pd.DataFrame()

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

def filter_by_sex(sex, df):
    return df[df["sex"] == sex]

# Cargar datos
LENGTH_DATA = sum(1 for _ in open(DATA_URL)) - 1 
df = load_data()

def main():
    st.title("Streamlit Dashboard")
    st.header("Welcome to Streamlit")
    st.write("by adsoft")
    st.write("Iker Gerardo Guevara Sanchez")
    st.write("zs22004366")
    st.image("foto.jpeg")

    st.subheader("Load Dataset")
    nrows = st.number_input("Number of rows to load", 1, LENGTH_DATA)
    df_subset = load_data(nrows)
    st.dataframe(df_subset)

    st.subheader("Search Names in Dataset")
    myname = st.text_input("Enter a name:")
    if myname:
        results = search_matches(myname, df)
        st.write(f"### Found {len(results)} matches:")
        st.dataframe(results)
    else:
        st.info("Please enter a name to search.")

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

    st.subheader("Filter by Gender")
    selected_sex = st.selectbox("Select Gender:", ["F", "M"])
    if st.button("Filter"):
        filtered_df = filter_by_sex(selected_sex, df)
        count = len(filtered_df)
        st.write(f"### Found {count} {'women' if selected_sex == 'F' else 'men'} in the dataset.")
        st.dataframe(filtered_df)

if __name__ == "__main__":
    main()
