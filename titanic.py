import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Cargar datos del Titanic
titanic_link = 'titanic.csv'
titanic_data = pd.read_csv(titanic_link)

# Cargar datos de Uber
DATE_COLUMN = 'date/time'
DATA_URL = ('uber_dataset.csv')

@st.cache_data  
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Configuración de la barra lateral
sidebar = st.sidebar
sidebar.title("Barra Lateral")
sidebar.write("Iker Gerardo Guevara Sanchez")
sidebar.write("zs22004366@estudiantes.uv.mx")
sidebar.image("credencial.jpeg")

today = datetime.date.today()
today_date = sidebar.date_input('Current date', today)
st.success(f'Current date: {today_date}')

# Sección Titanic
st.title('Titanic App')
selected_town = st.radio("Select Embark Town", titanic_data['embark_town'].dropna().unique())
st.write(f"Selected Embark Town: {selected_town}")

optionals = st.expander("Optional Configurations", True)

fare_min = optionals.slider("Minimum Fare", float(titanic_data['fare'].min()), float(titanic_data['fare'].max()), float(titanic_data['fare'].min()))
fare_max = optionals.slider("Maximum Fare", float(titanic_data['fare'].min()), float(titanic_data['fare'].max()), float(titanic_data['fare'].max()))

agree = st.checkbox("Show DataSet Overview?")
if agree:
    st.dataframe(titanic_data[(titanic_data['fare'] >= fare_min) & (titanic_data['fare'] <= fare_max) & (titanic_data['embark_town'] == selected_town)])

# Gráficos del Titanic
fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)
st.markdown("___")

fig2, ax2 = plt.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuánto pagaron las clases del Titanic?')
st.header("Gráfica de Barras del Titanic")
st.pyplot(fig2)
st.markdown("___")

fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Gráfica de Dispersión del Titanic")
st.pyplot(fig3)

# Mapa de San Francisco
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.title("San Francisco Map")
st.header("Using Streamlit and Mapbox")
st.map(map_data)

# Datos de Uber
st.title('Uber pickups in NYC')
data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)
