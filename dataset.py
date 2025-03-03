import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

st.set_page_config(page_title="Social Media Analytics", page_icon="📊")

# BD
@st.cache_data
def load_data():
    conn = sqlite3.connect("socialmedia.db")  
    query = "SELECT * FROM users" 
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = load_data()

st.image("logo.png", width=100) 
st.title("Analisis de Redes Sociales")
st.subheader("Autor: Iker Gerardo Guevara Sanchez")

#Filtros
st.sidebar.header("Opciones de visualización")
st.sidebar.image("credencial.jpeg")
n_rows = st.sidebar.slider("Número de filas a mostrar", 5, len(df), 10)

#Nombre
st.sidebar.header("Buscar usuario")
nombre_busqueda = st.sidebar.text_input("Nombre del usuario")

search_button = st.sidebar.button("Buscar Usuario")

#Genero
st.sidebar.header("Filtrar datos")
generos = st.sidebar.multiselect("Selecciona género", df["Gender"].dropna().unique())

data_filtered = df.copy()

if search_button and nombre_busqueda:
    data_filtered = data_filtered[data_filtered['Name'].astype(str).str.contains(nombre_busqueda, case=False, na=False)]

if generos:
    data_filtered = data_filtered[data_filtered["Gender"].isin(generos)]

st.write(f"Se encontraron {len(data_filtered)} resultados.")
st.dataframe(data_filtered.head(n_rows))

data_filtered["DOB"] = pd.to_datetime(data_filtered["DOB"], errors='coerce')
data_filtered["Age"] = data_filtered["DOB"].apply(lambda x: datetime.now().year - x.year if pd.notnull(x) else np.nan)

data_filtered["Num_Interests"] = data_filtered["Interests"].astype(str).apply(lambda x: len(x.split(",")) if x != "nan" else 0)

st.subheader("Distribución de edades por género")

# Histograma para los hombres
plt.figure(figsize=(8, 4))
sns.histplot(data=data_filtered[data_filtered["Gender"] == "Male"], x="Age", bins=20, color="blue", kde=False)
plt.title("Distribución de edades - Hombres")
plt.xlabel("Edad")
plt.ylabel("Cantidad de usuarios")
st.pyplot(plt)
plt.clf()

# Histograma para las mujeres
plt.figure(figsize=(8, 4))
sns.histplot(data=data_filtered[data_filtered["Gender"] == "Female"], x="Age", bins=20, color="pink", kde=False)
plt.title("Distribución de edades - Mujeres")
plt.xlabel("Edad")
plt.ylabel("Cantidad de usuarios")
st.pyplot(plt)
plt.clf()

st.write("Estos histogramas muestran la distribución de edades separada por género. Las barras azules representan a los hombres y las barras rosas a las mujeres.")

#Barras
st.subheader("Cantidad de usuarios por país")
top_countries = data_filtered["Country"].value_counts().head(10).index
data_filtered_top = data_filtered[data_filtered["Country"].isin(top_countries)]

country_counts = data_filtered_top["Country"].value_counts()
plt.figure(figsize=(8, 4))
sns.barplot(x=country_counts.values, y=country_counts.index, palette="viridis")
plt.xlabel("Cantidad de usuarios")
st.pyplot(plt)
plt.clf()

st.write("Esta gráfica muestra la cantidad de usuarios en los países más representados en la red social. Nos ayuda a entender dónde está la mayor parte de nuestra audiencia.")

# Scatter
st.subheader("Relación entre Edad y Número de Intereses en México")

data_mexico = data_filtered[data_filtered["Country"] == "Mexico"]

if not data_mexico.empty:
    plt.figure(figsize=(8, 6))
    
    colors = {"Male": "blue", "Female": "pink"}
    
    sns.scatterplot(
        data=data_mexico, 
        x="Age", 
        y="Num_Interests", 
        hue="Gender", 
        palette=colors, 
        s=100, 
        alpha=0.6
    )

    plt.title("Edad vs. Número de Intereses en México")
    plt.xlabel("Edad")
    plt.ylabel("Número de Intereses")

    plt.yticks(range(int(data_mexico["Num_Interests"].min()), int(data_mexico["Num_Interests"].max()) + 1))

    st.pyplot(plt)
else:
    st.write("No hay datos disponibles para México en la selección actual.")
