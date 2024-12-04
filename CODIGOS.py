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

# SEGUNDO CÓDIGO
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
