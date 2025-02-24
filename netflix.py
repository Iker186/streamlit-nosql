import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos(n_filas=500):
    df = pd.read_csv('movies.csv', encoding='latin1')
    return df.head(n_filas)

def main():
    st.title("Netflix app")
    st.write("Done! (using st.cache)")

    df = cargar_datos()

    st.sidebar.header("Filtros")
    
    st.sidebar.write("Iker Gerardo Guevara Sanchez")
    st.sidebar.write("zs22004366@estudiantes.uv.mx")
    st.sidebar.image("credencial.jpeg")

    mostrar_todos = st.sidebar.checkbox("Mostrar todos los filmes", value=True)
    
    name = st.sidebar.text_input("Título del filme :")
    if name:
        df = df[df['name'].str.contains(name, case=False, na=False)]

    directores = df['director'].dropna().unique()
    director_seleccionado = st.sidebar.selectbox("Seleccionar Director", options=["Todos"] + list(directores))
    if director_seleccionado != "Todos":
        df = df[df['director'] == director_seleccionado]

    st.subheader("Todos los filmes")
    st.dataframe(df)

if __name__ == '__main__':
    main()
