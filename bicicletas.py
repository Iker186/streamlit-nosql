import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data(nrows):
    df = pd.read_csv("citibike-tripdata.csv", nrows=nrows)
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['hour'] = df['started_at'].dt.hour
    df.rename(columns={'start_lat': 'lat', 'start_lng': 'lon'}, inplace=True)
    return df

data = load_data(500)

st.sidebar.title("Opciones")
show_data = st.sidebar.checkbox("Show raw data")
show_hist = st.sidebar.checkbox("Recorridos por hora")
hour = st.sidebar.slider("hour", 0, 23, 17)

st.sidebar.write("Iker Gerardo Guevara Sanchez")
st.sidebar.write("zs22004366@estudiantes.uv.mx")
st.sidebar.image("credencial.jpeg")

if show_data:
    st.subheader("Raw data")
    st.write(data)

filtered_data = data[data['hour'] == hour]

if show_hist:
    st.subheader("Numero de recorridos por hora")
    hourly_counts = data['hour'].value_counts().sort_index()
    fig, ax = plt.subplots()
    ax.bar(hourly_counts.index, hourly_counts.values)
    ax.set_xlabel("Hora del día")
    ax.set_ylabel("Número de recorridos")
    ax.set_title("Numero de recorridos por hora")
    st.pyplot(fig)

st.subheader("Mapa de puntos de inicio")
st.map(filtered_data[['lat', 'lon']])
