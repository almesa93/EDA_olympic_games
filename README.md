## EDA_olympic_games

### Introduccion

En el estudio que tiene lugar en este notebook, analizaremos los **Juegos Olímpicos verano** a lo largo de la historia, desde el 1896, que fueron los primeros de la era moderna, hasta los realizados en Río de Janeiro de 2016.

A continuación, analizaremos las distintas ediciones, observando los atletas participantes en cada una de ellas y viendo las cualidades físicas de todos ellos y los cambios que han ido surgiendo en estos, en caso de que los haya habido.

Finalmente, nos centraremos en la prueba de los **100 Metros Lisos** de la categoría de atletismo, que gracias a deportistas como Usain Bolt, se ha vuelto una de las más famosas. Basándonos en las condiciones físicas medias de cada época, compararemos dos de los más grandes atletas a lo largo de la historia, tanto de la prueba masculina como la femenina, con la finalidad de saber si sus físicos están en la media o están fuera de lo común (OUTLIER), lo que les hubiera permitido destacar por encima del resto de sus competidores

El notebook es el fichero principal del proyecto. En él, hacemos algunas de las transformaciones menores. El resto de las transformaciones y la realización de los gráficos, se han externalizado al fichero **olympics_func.py**, lo que ha permitido reducir el volumen de código en el notebook y empaquetar de mejor forma todo el código.

Así mismo, se ha creado un fichero adicional, **data_olympics.py** que contiene algunas variables y datos que serán necesarios para la ejecución de las funciones.

### ÍNDICE
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


### 1. DECLARACIÓN DE LIBRERíAS <a id='DECLARACION_DE_LIBRERIAS'></a>

Declaración de todas las librerías que se han utilizado para limpiar los datos y dibujar los gráficos que nos han ayudado a la realización del estudio, además de importar las funciones que hemos creado y los datos de los que hemos hablado anteriormente.


### 2. LECTURA DEL FICHERO <a id='LECTURA_DEL_FICHERO'></a>

Abrimos el fichero CSV obtenido de **KAGGLE** y lo guardamos en una variable para poder usarlo en el resto del archivo. Mostramos los primeros elementos para ver el aspecto que tiene el mismo y saber cómo trabajar con él.


### 3. LIMPIEZA DE LA INFORMACIÓN <a id='LIMPIEZA_DE_LA_INFORMACION'></a>

Llamamos a la función **df_clean(df)**, que realiza la limpieza de los datos del CSV. Véase la función en el fichero **olimpycs_func.py** para conocer más acerca del funcionamiento de la misma.


### 4. ATLETAS POR EDICIÓN <a id='ATLETAS_POR_EDICION'></a>

Dibujo de los gráficos en los que analizar los participantes por año de cada uno de los Juegos Olímpicos.

Introducimos los datos necesarios para la realización del gráfico. Una vez tenemos todo, llamamos a la función **create_trace_scatter()** para realizar el diagrama de líneas que muestra la evolución de la cantidad de atletas que han participado a lo largo de la historia. Para más información acerca de la función, véase el fichero **olimpycs_func.py**.

Al final de la representación, llamamos a la función **save_graph()** de nuestro repositorio de funciones del fichero **olimpycs_func.py**. Esta función guarda los gráficos en un perfil de la web de **Plotly**, que nos servirá para luego poder ejecutar los gráficos interactivos en una presentación PowerPoint.


### 5. DELEGACIONES POR EDICIÓN <a id='DELEGACIONES_POR_EDICION'></a>

Dibujo de los gráficos en los que analizar las delegaciones por año que han ido en cada uno de los Juegos Olímpicos, que podremos comparar con el anterior.

Introducimos los datos necesarios para la realización del gráfico. Una vez tenemos todo, llamamos a la función **create_trace_scatter()** para realizar el diagrama de líneas que muestra la evolución de la cantidad de atletas que han participado a lo largo de la historia. Para más información acerca de la función, véase el fichero **olimpycs_func.py**.

Al final de la representación, llamamos a la función **save_graph()** de nuestro repositorio de funciones del fichero **olimpycs_func.py**. Esta función guarda los gráficos en un perfil de la web de **Plotly**, que nos servirá para luego poder ejecutar los gráficos interactivos en una presentación PowerPoint.


### 6. FILTRO DE ATLETAS <a id='FILTRO_DE_ATLETAS'></a>

Los Juegos Olímpicos tienen eventos tanto para hombres como para mujeres desde el año 1928 hasta 2016. Aquí dividimos el dataframe en dos, uno para todas las competiciones masculinas y otro para las femeninas. Debido a causas históricas, las mujeres no pudieron participar en los Juegos Olímpicos entre las ediciones de 1896 de Atenas y las de Amsterdam 1928, por lo que el volumen de datos de las mujeres será mucho menor.

El primer filtro que hemos realizado, ha sido acotar las competiciones a considerar. Tras observar los datos, vamos a quedarnos con los eventos más representativos, que son aquellas que pertenecen a la categoría de Atletismo.

Otro de los factores a tener en cuenta, ha sido esos eventos por los que hemos filtrado. Para ver una evolución correcta a lo largo de la historia, hemos escogido aquellos deportes que se han repetido en muchas de las ediciones.

Como tenemos una gran cantidad de datos, necesitaremos algún tipo de filtro más, por lo que nos hemos quedado solo con los medallistas, ya que nos interesa principalmente las cualidades de los mejores.

Por último, sacamos las cualidades físicas medias de todos ellos. En este caso consideraremos la edad, la altura y el peso.

En este apartado, llamamos a 3 funciones distintas para la transformación:

- **sex_filter()**: divide por sexo el dataframe
- **athletes_filter()**: filtra la información para quedarnos con los medallistas y con aquellos deportes que más se han repetido.
- **physical_filter()**: extrae las cualidades físicas medias de cada 

Véase el fichero **olimpycs_func.py** para más información sobre las funciones.


### 7. AÑOS DE ESTUDIO, DICCIONARIO DE COLORES Y DEPORTES ESTUDIADOS <a id='PREPARACION_DE_ESTUDIO'></a>

No se pueden estudiar todas las olimpiadas que se han celebrado a lo largo de la historia, por lo que vamos a estudiar solo algunas de ellas, espaciadas varias ediciones entre sí para tener datos representativos.

Finalmente, filtraremos por los elementos comunes a todas ellas.

Para realizar todo lo descrito, llamaremos a las siguientes funciones:
- **year_filter**: devuelve la lista de años en los que se han celebrado los Juegos Olímpicos.
- **year_dict**: devuelve un diccionario [año]:[rgba] para pintar la gráfica y la lista de los años que se van a estudiar.
- **common_categories**: devuelve un dataframe los Juegos Olímpicos que se van a estudiar, las disciplinas y los valores finales.


### 8. CUALIDADES FÍSICAS EN ATLETISMO MASCULINO <a id='FISICO_M'></a>

Con todos los datos preparados para tratar, en este apartado se realizan los gráficos comparativos de los datos de la complexión física y la edad de los atletas de la categoría masculina a lo largo de la historia en distintas disciplinas.

Para ello, introducimos los datos necesarios para la realización del gráfico. Una vez tenemos todo, llamamos a la función **create_trace_scatter()** para realizar el diagrama. Para más información acerca de la función, véase el fichero **olimpycs_func.py**.

Al final de la representación, llamamos a la función **save_graph()** de nuestro repositorio de funciones del fichero **olimpycs_func.py**. Esta función guarda los gráficos en un perfil de la web de **Plotly**, que nos servirá para luego poder ejecutar los gráficos interactivos en una presentación PowerPoint.


### 9. CUALIDADES FÍSICAS EN ATLETISMO FEMENINO <a id='FISICO_F'></a>

En este apartado se realizan los gráficos comparativos de los datos de la complexión física y la edad de los atletas de la categoría femenina a lo largo de la historia en distintas disciplinas.

Para ello, introducimos los datos necesarios para la realización del gráfico. Una vez tenemos todo, llamamos a la función **create_trace_scatter()** para realizar el diagrama. Para más información acerca de la función, véase el fichero **olimpycs_func.py**.

Al final de la representación, llamamos a la función **save_graph()** de nuestro repositorio de funciones del fichero **olimpycs_func.py**. Esta función guarda los gráficos en un perfil de la web de **Plotly**, que nos servirá para luego poder ejecutar los gráficos interactivos en una presentación PowerPoint.


### 10. OBTENCIÓN DE INFORMACIÓN DE LA PRUEBA DE 100 METROS LISOS MEDIANTE WEB SCRAPING <a id='WEB_SCRAPING'></a>

Los ficheros descargados de **KAGGLE** no disponían de la información de los tiempos de la prueba en cuestión. Debido a esto, es necesario obtenerlo mediante Web Scraping con BeautifulSoup de la página web oficial de los Juegos Olímpicos (https://olympics.com/en/olympic-games/olympic-results). Para ello, primero llamamos a la función **juegos_ano_olympics()**, del fichero de funciones **olimpycs_func.py** que se encargará de descargar una lista con binomios de tipo **['juegos', 'año']** con cada uno de los JJOO que han existido hasta 2016. Esta lista de listas queda almacenada en una variable.

Lo siguiente es llamar a la función **request_100m()**, también en el mismo repositorio de funciones, que con estos binomios obtenidos con la función anterior, hace otro web scraping para obtener toda la información acerca de los ganadores con sus tiempos en cada uno de los Juegos Olímpicos de la prueba de 100 Metros Lisos. Esta información la convierte en un dataframe y también genera un archivo en formato CSV para no tener que hacer la request cada vez que se quiera ejecutar el programa.


### 11. LIMPIEZA DE LOS DATOS DE LOS 100 METROS LISOS <a id='LIMPIEZA_100M'></a>

En este apartado, llamamos a la función **clean_time()** que sirve para limpiar los datos de los tiempos, ya que unos tienen una forma tipo "10.3w", por lo que hubo que quitar el string final y pasar todo a tipo float, ya que detecta todos los valores como un string.

Véase el archivo **olimpycs_func.py** para obtener más información acerca de esta función.


### 12. REPRESENTACIÓN DE LOS DATOS DE LOS 100 METROS LISOS <a id='GRAFICO_100M'></a>

Con todos los datos limpios y en el formato correcto, representamos el gráfico que muestra los ganadores de todos los Juegos Olímpicos a lo largo de la historia.

Para ello, introducimos los datos necesarios para la realización del gráfico. Una vez tenemos todo, llamamos a la función **create_trace_scatter()** para realizar el diagrama. Para más información acerca de la función, véase el fichero **olimpycs_func.py**.

Al final de la representación, llamamos a la función **save_graph()** de nuestro repositorio de funciones del fichero **olimpycs_func.py**. Esta función guarda los gráficos en un perfil de la web de **Plotly**, que nos servirá para luego poder ejecutar los gráficos interactivos en una presentación PowerPoint.
