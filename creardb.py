import pandas as pd
import sqlite3

# Cargar datos desde el CSV
df = pd.read_csv("socialmedia.csv")

# Conectar a SQLite (crea la base de datos si no existe)
conn = sqlite3.connect("socialmedia.db")

# Guardar el DataFrame en la base de datos
df.to_sql("users", conn, if_exists="replace", index=False)

# Cerrar conexión
conn.close()

print("Base de datos creada exitosamente.")
