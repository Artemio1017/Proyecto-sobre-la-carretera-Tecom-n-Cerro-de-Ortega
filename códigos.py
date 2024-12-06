# -*- coding: utf-8 -*-
"""CÓDIGOS

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1shFcX6w_uMZrO1MCWdx6BHc1MaqawfUB

**CÓDIGO PARA CALCULAR LA FUERZA DE LA CARRETERA Y PREVENIR BACHES**
"""

import numpy as np
#Parámetros del material de la carretera
modulo_elasticidad = 3e9  #en Pascales (ejemplo: asfalto)
espesor_carretera = 0.15  #en metros
limite_tension = 2.5e6    #tensión máxima permitida en Pascales (ejemplo)
#Parámetros de la carga
carga_aplicada = 10000    #en Newtons (peso del vehículo, por ejemplo)
area_contacto = 0.01      #en metros cuadrados (área de contacto de la rueda)
#Calcular presión en el área de contacto
presion_contacto = carga_aplicada / area_contacto  # en Pascales
#Calcular tensión en la carretera (simulación simplificada usando esfuerzo máximo)
tension_generada = presion_contacto * espesor_carretera / modulo_elasticidad
#Comparar con el límite de tensión
if tension_generada < limite_tension:
    print("La carretera soporta la carga sin generar baches.")
else:
    print("El material de la carretera está sometido a demasiada tensión. Se podrían generar baches.")
#Imprimir los resultados
print(f"Tensión generada: {tension_generada:.2e} Pa")
print(f"Límite de tensión: {limite_tension:.2e} Pa")

"""**CÓDIGO PARA EL CÁLCULO DE PRESUPUESTO**"""

#Parámetros iniciales
costo_reparacion_por_bache = 1164  #Costo de reparar un bache (en dólares)
cantidad_baches = 100             #Cantidad total de baches en la carretera
presupuesto_total = 20000        #Presupuesto disponible (en dólares)
#Calcular el costo total de reparación
costo_total_reparacion = cantidad_baches * costo_reparacion_por_bache
#Comparar con el presupuesto disponible
if costo_total_reparacion <= presupuesto_total:
    sobrante = presupuesto_total - costo_total_reparacion
    print("El presupuesto es suficiente para reparar todos los baches.")
    print(f"Dinero sobrante después de las reparaciones: ${sobrante:.2f}")
else:
    print("El presupuesto no es suficiente para reparar todos los baches.")
    baches_reparables = presupuesto_total // costo_reparacion_por_bache
    print(f"Se pueden reparar aproximadamente {baches_reparables:.0f} baches con el presupuesto actual.")
#Imprimir resultados
print(f"Costo total de reparación: ${costo_total_reparacion:.2f}")
print(f"Presupuesto disponible: ${presupuesto_total:.2f}")

"""**CODIGO PARA MOSTRAR EN UN MAPA HTML LA CARRETERA Y DISTINTOS PUNTOS SOBRE ELLEA**"""

pip install pandas folium geopy openpyxl

import pandas as pd
import folium
from geopy.distance import geodesic
from shapely.geometry import Polygon

# Crear un archivo Excel con datos de latitud y longitud
datos = {
    "latitud": [18.940366,18.941291,18.943720,18.943696,18.938971,18.934044,18.932349,18.925118,18.909256,18.897659],
    "longitud": [-103.894279,-103.891595,-103.888927,-103.883153,-103.875472,-103.867526,-103.860385,-103.854995,-103.854167,-103.859358]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(datos)

# Guardar el DataFrame como archivo Excel
archivo_excel = "datos_geograficos.xlsx"
df.to_excel(archivo_excel, index=False)
print(f"Archivo Excel creado: {archivo_excel}")

import pandas as pd
import folium
from geopy.distance import geodesic
from shapely.geometry import Polygon
from IPython.display import display
from google.colab import files
# Paso 2: Leer el archivo Excel
df = pd.read_excel(archivo_excel)

# Verifica que las columnas de latitud y longitud existan
if not {'latitud', 'longitud'}.issubset(df.columns):
    raise ValueError("El archivo debe contener columnas llamadas 'latitud' y 'longitud'.")

# Crear un mapa centrado en el primer punto
lat_inicial = df.iloc[0]['latitud']
lon_inicial = df.iloc[0]['longitud']
mapa = folium.Map(location=[lat_inicial, lon_inicial], zoom_start=12)

# Agregar puntos al mapa
for _, row in df.iterrows():
    folium.Marker([row['latitud'], row['longitud']], popup=f"({row['latitud']}, {row['longitud']})").add_to(mapa)

# Guardar el mapa como un archivo HTML
nombre_mapa = "mapa_interactivo.html"
mapa.save(nombre_mapa)
print("Mapa generado: mapa_interactivo.html")

# Descargar el mapa interactivo en Colab
files.download(nombre_mapa)

# Calcular la distancia total entre puntos consecutivos
distancia_total = 0
puntos = list(zip(df['latitud'], df['longitud']))

for i in range(len(puntos) - 1):
    distancia_total += geodesic(puntos[i], puntos[i + 1]).kilometers

print(f"Distancia total (km): {distancia_total:.2f}")

# Calcular el área aproximada si los puntos forman un polígono cerrado
if len(puntos) > 2:
    polygon = Polygon(puntos)
    area = polygon.area  # El área está en unidades cuadradas de grados
    print(f"Área aproximada en grados cuadrados: {area:.6f}")
else:
    print("No es posible calcular el área con menos de 3 puntos.")

