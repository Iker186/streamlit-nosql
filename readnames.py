import streamlit as st
import pandas as pd

# Título de la app
st.title("Visualización de Datos")

# Cargar el archivo CSV
file_path = "dataset.csv"  # Asegúrate de que este es el nombre correcto
try:
    df = pd.read_csv(file_path)

    # Mostrar los datos
    st.write("Vista previa del dataset:")
    st.dataframe(df)

except FileNotFoundError:
    st.error(f"El archivo {file_path} no se encontró. Asegúrate de que está en el mismo directorio que este script.")
except Exception as e:
    st.error(f"Ocurrió un error al cargar el archivo: {e}")

