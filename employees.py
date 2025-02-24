import streamlit as st
import pandas as pd

# Función para cargar datos con cache
@st.cache_data
def load_data(n=500):
    df = pd.read_csv('Employees.csv')
    return df.head(n)

# Cargar datos
employees = load_data()

# Título y descripción
st.title("Dashboard de Empleados")
st.header("Análisis de Datos de Empleados")
st.write("Este proyecto analiza la información de empleados para evaluar deserción y otros indicadores clave.")

# Sidebar con información adicional
st.sidebar.write("Iker Gerardo Guevara Sanchez")
st.sidebar.write("zs22004366@estudiantes.uv.mx")
st.sidebar.image("credencial.jpeg")

# Filtros
st.sidebar.header("Filtros")

# Buscador de empleados
search_id = st.sidebar.text_input("Buscar por Employee_ID")
search_hometown = st.sidebar.text_input("Buscar por Hometown")
search_unit = st.sidebar.text_input("Buscar por Unit")

# Filtro por nivel educativo con opción de "Mostrar Todos"
education_levels = employees['Education_Level'].unique().tolist()
education_levels.insert(0, "Mostrar Todos")  # Agregar opción "Mostrar Todos"
selected_level = st.sidebar.selectbox("Filtrar por Nivel Educativo", education_levels)

# Filtro por ciudad con opción de "Mostrar Todos"
cities = employees['Hometown'].unique().tolist()
cities.insert(0, "Mostrar Todos")  # Agregar opción "Mostrar Todos"
selected_city = st.sidebar.selectbox("Filtrar por Ciudad", cities)

# Filtro por unidad funcional con opción de "Mostrar Todos"
units = employees['Unit'].unique().tolist()
units.insert(0, "Mostrar Todos")  # Agregar opción "Mostrar Todos"
selected_unit = st.sidebar.selectbox("Filtrar por Unidad Funcional", units)

# Aplicar filtros a la tabla
filtered_data = employees

# Asegurarse de que el ID sea tratado como cadena para la búsqueda
if search_id:
    filtered_data = filtered_data[filtered_data['Employee_ID'].str.contains(search_id, case=False)]

if search_hometown:
    filtered_data = filtered_data[filtered_data['Hometown'].str.contains(search_hometown, case=False)]
if search_unit:
    filtered_data = filtered_data[filtered_data['Unit'].str.contains(search_unit, case=False)]

if selected_level != "Mostrar Todos":
    filtered_data = filtered_data[filtered_data['Education_Level'] == selected_level]

if selected_city != "Mostrar Todos":
    filtered_data = filtered_data[filtered_data['Hometown'] == selected_city]

if selected_unit != "Mostrar Todos":
    filtered_data = filtered_data[filtered_data['Unit'] == selected_unit]

# Mostrar resultados filtrados
st.dataframe(filtered_data)
st.write(f"Total de empleados encontrados: {len(filtered_data)}")

# Gráficas
import matplotlib.pyplot as plt

# Histograma de empleados por edad
st.header("Histograma de Empleados por Edad")
plt.hist(filtered_data['Age'], bins=10, color='skyblue')
plt.xlabel('Edad')
plt.ylabel('Cantidad de Empleados')
plt.title('Distribución de Edad')
st.pyplot(plt)

# Gráfica de frecuencias por Unidad Funcional
st.header("Frecuencias por Unidad Funcional")
unit_counts = filtered_data['Unit'].value_counts()
plt.figure(figsize=(10, 5))
unit_counts.plot(kind='bar', color='orange')
plt.xlabel('Unidad Funcional')
plt.ylabel('Número de Empleados')
plt.title('Empleados por Unidad Funcional')
st.pyplot(plt)

# Análisis de deserción: Índice de deserción por ciudad
st.header("Índice de Deserción por Ciudad")
desertion_by_city = filtered_data.groupby('Hometown')['Attrition_rate'].mean()
desertion_by_city.plot(kind='bar', color='red')
plt.title('Índice de Deserción por Ciudad')
plt.ylabel('Tasa de Deserción')
st.pyplot(plt)

# Edad vs Tasa de Deserción
st.header("Edad vs Tasa de Deserción")
plt.scatter(filtered_data['Age'], filtered_data['Attrition_rate'], color='purple')
plt.xlabel('Edad')
plt.ylabel('Tasa de Deserción')
plt.title('Relación Edad - Tasa de Deserción')
st.pyplot(plt)

# Tiempo de Servicio vs Tasa de Deserción
st.header("Tiempo de Servicio vs Tasa de Deserción")
plt.scatter(filtered_data['Time_of_service'], filtered_data['Attrition_rate'], color='green')
plt.xlabel('Tiempo de Servicio')
plt.ylabel('Tasa de Deserción')
plt.title('Relación Tiempo de Servicio - Tasa de Deserción')
st.pyplot(plt)
