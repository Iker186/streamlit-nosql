import streamlit as st
st.title("App side bar")

sidebar = st.sidebar

sidebar.title("barra lateral")

sidebar.write("Aqui van los elementos de entrada.")
sidebar.write('Iker Gerardo Guevara Sanchez')
sidebar.write('zs22004366@estudiantes.uv.mx')
sidebar.image("credencial.jpeg")

st.header("Informacion sobre el Conjunto de Datos")
st.header("Descripcion de los datos")

st.write("""
Este es un simple ejemplo de una app para predecir

¡Esta app predice mis datos!
""")
