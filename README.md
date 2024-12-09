# Proyecto-sobre-la-carretera-Tecomán-Cerro-de-Ortega
El conteo de baches totales sobre esta carretera y el como esto afecta a toda la comunidad
# Título del Proyecto
**Autores:**
Gómez Padilla Artemio Gabriel

## Introducción
La carretera que conecta Cerro de Ortega con Tecomán constituye una vía esencial para la movilidad y el desarrollo socioeconómico de la región. Sin embargo, su actual estado de deterioro representa un grave desafío para la seguridad vial, la eficiencia del tránsito y la calidad de vida de los habitantes. Este tramo es utilizado diariamente por un volumen significativo de conductores, incluidos agricultores, transportistas y personas que dependen de él para sus actividades económicas, educativas y sociales. El deterioro de la vía, caracterizado por la presencia de baches profundos, fisuras y una deficiente señalización, ha generado numerosos accidentes, volcaduras y daños considerables a vehículos, afectando a particulares y sectores estratégicos como el transporte de productos agrícolas hacia mercados regionales y nacionales.  Frente a esta problemática, el proyecto tiene como objetivo principal la rehabilitación integral de esta carretera para garantizar la seguridad de los ciudadanos, mejorar el flujo vehicular y contribuir al desarrollo económico de la región. Las acciones propuestas incluyen la identificación y reparación de baches, la optimización del drenaje para prevenir acumulaciones de agua durante lluvias, y la mejora de la señalización vial para reducir accidentes. Además, se propone incorporar materiales sostenibles y técnicas innovadoras de construcción que no solo reduzcan costos, sino que también minimicen el impacto ambiental. 
El impacto positivo de este proyecto es amplio y tangible. Por un lado, mejorar la infraestructura vial reducirá significativamente los accidentes de tránsito, protegerá los vehículos de daños costosos y mejorará la experiencia de los conductores. Por otro lado, al optimizar esta vía estratégica, se fortalecerá la economía regional, permitiendo un transporte más eficiente de bienes agrícolas y comerciales, y potenciando la productividad de las comunidades circundantes. A largo plazo, la renovación de la carretera sentará las bases para un desarrollo sostenible, incrementando la conectividad y calidad de vida de miles de personas que dependen de esta vía diariamente.La necesidad de intervenir de manera urgente no solo responde a los crecientes reclamos de la población, que ha recurrido a manifestaciones y bloqueos en señal de protesta, sino también a la importancia estratégica de esta carretera para la actividad comercial e industrial de la región. Ignorar esta situación podría no solo aumentar la frecuencia de accidentes y el desgaste de los vehículos, sino también agravar los problemas de movilidad y afectar directamente la competitividad económica de la región.
En resumen, este proyecto de rehabilitación representa una oportunidad clave para transformar una vía en un motor de desarrollo. A través de una planificación detallada, la participación de la comunidad y la implementación de soluciones innovadoras, se busca no solo reparar una carretera, sino también fortalecer los cimientos del progreso económico y social de una región que depende profundamente de su infraestructura vial.


## Desarrollo
El proyecto tiene como objetivo principal la renovación integral de la carretera Cerro de Ortega-Tecomán, que actualmente presenta un deterioro crítico que afecta tanto la seguridad vial como el desarrollo socioeconómico de la región. Este tramo es fundamental para el transporte diario de personas y mercancías, conectando centros productivos agrícolas y comerciales con mercados regionales. La propuesta busca abordar problemas clave como baches, drenaje deficiente y la falta de señalización adecuada, garantizando un impacto positivo en la movilidad, la calidad de vida de la comunidad y el desarrollo económico sostenible. El enfoque estratégico incluye tanto acciones correctivas inmediatas como planes a largo plazo, integrando un análisis técnico profundo, la participación activa de la comunidad y la aplicación de soluciones innovadoras.
Herramientas Utilizadas
Sistemas de Información Geográfica: Se emplearán para mapear baches, monitorear avances y optimizar la planificación de reparaciones.
Encuestas y talleres participativos: Recopilar opiniones y necesidades de los usuarios y comunidades locales.
Metodología de estimación de costos: Se utilizarán índices de precios actualizados para materiales y mano de obra, contemplando factores climáticos y contingencias.
Indicadores Clave de Desempeño: Se definirán medidas específicas para medir el progreso, eficiencia y calidad del proyecto.
Metodología
1. Diagnóstico:
Se realizará una evaluación del estado actual de la carretera, identificando baches, fallos en el drenaje y problemas de señalización.
2. Planificación y Cálculo de Costos:
Inventario de baches: Clasificación detallada de baches por tamaño, profundidad y tipo de pavimento.
Estimación de costos unitarios: Basada en materiales, mano de obra y equipo necesario.
Contingencias: Adición de un porcentaje para cubrir imprevistos.
La fórmula general utilizada será:
Costo total = Σ (Número de baches * Costo unitario por bache) + Costos indirectos + Contingencia.
3. Ejecución:
Se implementarán reparaciones priorizando materiales sostenibles y técnicas de bajo impacto ambiental, asegurando una mayor durabilidad y menor afectación ecológica.
4. Participación Ciudadana:
Se organizarán talleres y encuestas para incorporar las opiniones y expectativas de la población local, fortaleciendo la transparencia y aceptación del proyecto.
5. Monitoreo y Evaluación:
El avance será medido con indicadores clave como la reducción de accidentes, calidad de las reparaciones y satisfacción de los usuarios. Se usará el SIG para actualizar y visualizar el progreso.

**Funcionamiento de los códigos utilizados**

**PRIMER CÓDIGO**
CÓDIGO PARA CALCULAR LA FUERZA DE LA CARRETERA Y PREVENIR BACHES.
Este código utiliza la libreria **NUMPY** para poder hacer todos los cálculos necesarios. Este toma en cuanta 3 principios básicos para la resistencia de un material al recibir una fuerza. Esta es la resistencia en Pascales del material (asfalto=3e9), el grosor del material(0.15 m) y el límite de tensión(2.5e6). Partiendo desde estos 3 valores ya se podría hacer un cálculo, pero falta lo escencial, la carga que se le aplica, esta puede variar dependiendo de si se trata de un carro, una camioneta o un camión, pero mayormente son carros los que pasen así que se tomó en cuenta este para el cálculo (1000kg). Para que el código funcione correctamente se agregó un valor adicional que es el peso en metro cuadrados de la llanta sobre el asfalto, que es de (0.2).
Los resultados son mostrados en pascales.
Debo agregar que se pueden hacer modificaciones en los parámetros del cálculo dependiendo del material que se quiere estudiar, así que se puede "jugar" con eso.

**Resultado**

![image](https://github.com/user-attachments/assets/860dca4a-f886-4d48-849d-741553a832bb)

**SEGUNDO CÓDIGO**
CÓDIGO PARA EL CÁLCULO DE PRESUPUESTO.
Este código no es tan complejo como el anterior, en este no es necesario instalar ninguna libreria ya que solo utiliza las funciones básicas de multiplicación, división, suma y resta.
Lo primero es ingresar los datos necesarios que es el costo de la reparación de los baches($1164), la cantidad de baches (100) y el presupuesto con el que se cuenta ($20000).
Con esos datos primero multiploca el costo por bache por la cantidad de baches, para después hacer una comparación entre el costo total y el prsupuesto con el que se cuenta. Si el presupuesto es mayor al costo total, nos mostrará una resta entre estas, sino es así solo nos dirá que el presupuesto es insuficiente.
También se puede jugar con los datos que se quieran introducir y el código funcionará perfectamente.

**Resultado**

![image](https://github.com/user-attachments/assets/150a8fd2-8f76-4422-9981-5bf1c9095496)

**TERCER CÓDIGO**
CODIGO PARA MOSTRAR EN UN MAPA HTML LA CARRETERA Y DISTINTOS PUNTOS SOBRE ELLA.
Este es el código más complejo de los 3 y el que más librerias necesita. En primer lugar es necesario ingresar el siguiente código: "pip install pandas folium geopy openpyxl" ya que este nos instala las librerias necesarias para después importarlas al código, tales como **FOLIUM** y **PANDAS** por ejemplo.
Al ya tener estas librerias instaladas es necesario ingresar las coordenadas de los distintos puntos de la carretera, camino o cualquier lugar que querramos mostrar, esto en formato **LATITUD** y **LONGITUD** tales como las mías:

 **latitud: [18.940366,18.941291,18.943720,18.943696,18.938971,18.934044,18.932349,18.925118,18.909256,18.897659]**
   
 **longitud: [-103.894279,-103.891595,-103.888927,-103.883153,-103.875472,-103.867526,-103.860385,-103.854995,-103.854167,-103.859358]**

Ahora en base a estas coordenadas, se pueden representar en un mapa HTML, al crearse nos manda a otra pa´gina donde se encuentra representada por puntos de identificación, el tramo de la carretera.
En el mismo código hace el cálculo total de la distancia entre la coordenada inicial y la final representada en Km.
Se pueden cambiar las coordenadas que yo ingresé por las que necesites y el código te lo representará.

**Resultado**

![image](https://github.com/user-attachments/assets/63c3ec6d-0496-481a-ab7a-b3db4be72db4)

![image](https://github.com/user-attachments/assets/0d2b0899-d847-4b77-9e8e-5aeb888e483c)


## Manejo de Datos
![image](https://github.com/user-attachments/assets/46f1f3dc-a5c6-491b-9e1a-b486cc9f0dd6)
![image](https://github.com/user-attachments/assets/da302f57-9857-4417-afe9-e9d67f101a5d)


## Identificación del tramo de carretera en ArcGIS
![carre_tecoman_co](https://github.com/user-attachments/assets/f1298275-bb71-40b3-ba61-2559a76ff068)


## Conclusiones
La carretera Cerro de Ortega - Tecomán desempeña un papel crucial en la conectividad y el desarrollo económico de la región, pero su deterioro actual representa un desafío significativo para la seguridad vial y la eficiencia del tránsito. Este proyecto tiene como meta abordar de manera integral los problemas detectados, como los baches, la falta de señalización adecuada y las deficiencias en el drenaje. A través de estrategias de planificación eficiente, el uso de materiales sostenibles y la participación activa de las comunidades afectadas, se busca no solo reparar la infraestructura existente, sino también sentar las bases para un desarrollo vial sostenible a largo plazo.
La implementación de este plan contribuirá directamente a mejorar la calidad de vida de los habitantes al reducir accidentes, facilitar el transporte de mercancías y promover una movilidad más segura y fluida. Además, al priorizar la inversión en infraestructura vial, se fortalecerá la economía regional, garantizando que la carretera sea una herramienta clave para el progreso local. Este proyecto destaca la importancia de una gestión eficiente de recursos, la colaboración entre actores gubernamentales y ciudadanos, y la adopción de soluciones innovadoras que aseguren el éxito del proyecto y sus beneficios a largo plazo.
