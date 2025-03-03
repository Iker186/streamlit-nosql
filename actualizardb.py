import sqlite3
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Conectar a la base de datos SQLite
conn = sqlite3.connect("socialmedia.db")
cursor = conn.cursor()

# Verificar si las columnas ya existen
cursor.execute("PRAGMA table_info(users)")
columns = [col[1] for col in cursor.fetchall()]

if "Latitude" not in columns or "Longitude" not in columns:
    cursor.execute("ALTER TABLE users ADD COLUMN Latitude REAL")
    cursor.execute("ALTER TABLE users ADD COLUMN Longitude REAL")
    conn.commit()

# Inicializar el geolocalizador
geolocator = Nominatim(user_agent="socialmedia_app")

# Función para obtener coordenadas
def obtener_coordenadas(city, country):
    try:
        location = geolocator.geocode(f"{city}, {country}", timeout=10)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return None, None

# Cargar datos desde la base de datos
df = pd.read_sql("SELECT * FROM users", conn)

# Aplicar la función a cada fila y actualizar la base de datos
for index, row in df.iterrows():
    if pd.isnull(row["Latitude"]) or pd.isnull(row["Longitude"]):
        lat, lon = obtener_coordenadas(row["City"], row["Country"])
        if lat and lon:
            cursor.execute("UPDATE users SET Latitude=?, Longitude=? WHERE UserID=?", (lat, lon, row["UserID"]))
            conn.commit()
        time.sleep(1)  # Evitar bloquear la API

# Cerrar conexión
conn.close()
print("Base de datos actualizada con coordenadas.")
