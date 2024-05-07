import os
import django
from django.db import connection

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')
django.setup()

# Consulta SQL para obtener los inmuebles por comunas
consulta_sql = """
    SELECT nombre, descripción
    FROM tu_app_tu_modelo
    WHERE tipo = 'arriendo' AND comuna = 'nombre_de_la_comuna';
"""

# Ejecutar la consulta SQL
with connection.cursor() as cursor:
    cursor.execute(consulta_sql)
    resultados = cursor.fetchall()

# Guardar los resultados en un archivo de texto
with open('inmuebles_por_comuna.txt', 'w') as archivo:
    for nombre, descripcion in resultados:
        archivo.write(f"Nombre: {nombre}\nDescripción: {descripcion}\n\n")
        
        
        
        
        
        
        
        
        