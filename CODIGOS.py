#PRIMER CÓDIGO
#Código para calcular la fuerza en la carretera y prevenir baches
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
