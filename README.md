# EDA_olympic_games

## Introduccion

En el estudio que tiene lugar en este notebook, analizaremos los **Juegos Olímpicos verano** a lo largo de la historia, desde el 1896, que fueron los primeros de la era moderna, hasta los realizados en Río de Janeiro de 2016.

A continuación, analizaremos las distintas ediciones, observando los atletas participantes en cada una de ellas y viendo las cualidades físicas de todos ellos y los cambios que han ido surgiendo en estos, en caso de que los haya habido.

Finalmente, nos centraremos en la prueba de los **100 Metros Lisos** de la categoría de atletismo, que gracias a deportistas como Usain Bolt, se ha vuelto una de las más famosas. Basándonos en las condiciones físicas medias de cada época, compararemos dos de los más grandes atletas a lo largo de la historia, tanto de la prueba masculina como la femenina, con la finalidad de saber si sus físicos están en la media o están fuera de lo común (OUTLIER), lo que les hubiera permitido destacar por encima del resto de sus competidores

El notebook es el fichero principal del proyecto. En él, hacemos algunas de las transformaciones menores. El resto de las transformaciones y la realización de los gráficos, se han externalizado al fichero **olympics_func.py**, lo que ha permitido reducir el volumen de código en el notebook y empaquetar de mejor forma todo el código.

Así mismo, se ha creado un fichero adicional, **data_olympics.py** que contiene algunas variables y datos que serán necesarios para la ejecución de las funciones.


1. [DECLARACIÓN DE LIBRERÍAS](#DECLARACION_DE_LIBRERIAS)
2. [LECTURA DEL FICHERO](#LECTURA_DEL_FICHERO)
3. [LIMPIEZA DE LA INFORMACIÓN](#LIMPIEZA_DE_LA_INFORMACION)
4. [ATLETAS POR EDICIÓN](#ATLETAS_POR_EDICION)
5. [DELEGACIONES POR EDICIÓN](#DELEGACIONES_POR_EDICION)
6. [FILTRO DE ATLETAS](#FILTRO_DE_ATLETAS)
7. [AÑOS DE ESTUDIO, DICCIONARIO DE COLORES Y DEPORTES ESTUDIADOS](#PREPARACION_DE_ESTUDIO)
8. [CUALIDADES FÍSICAS EN ATLETISMO MASCULINO](#FISICO_M)
9. [CUALIDADES FÍSICAS EN ATLETISMO FEMENINO](#FISICO_F)
10. [OBTENCIÓN DE INFORMACIÓN DE LA PRUEBA DE 100 METROS LISOS MEDIANTE WEB SCRAPING](#WEB_SCRAPING)
11. [LIMPIEZA DE LOS DATOS DE LOS 100 METROS LISOS](#LIMPIEZA_100M)
12. [REPRESENTACIÓN DE LOS DATOS DE LOS 100 METROS LISOS](#GRAFICO_100M)

ANEXO 1: olimpycs_func.py

ANEXO 2: data_olympics.py
