'''Declaración de librerías'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly
plotly.offline.init_notebook_mode()
import plotly.graph_objs as go
from plotly.graph_objs.scatter.marker import Line
from plotly.subplots import make_subplots
from plotly.offline import iplot
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls

def juegos_ano_olympics(URL):

    '''Esta función saca una lista con binomios de tipo ['juegos', 'año'] con cada uno de los JJOO que han existido hasta 2016
    y retorna esta lista de listas. Para ello, tendremos que darle como valor la URL.'''

    r = requests.get('https://olympics.com/en/olympic-games/olympic-results')
    soup = BeautifulSoup(r.text, 'lxml')

    juegos = soup.find_all(class_='styles__ItemButton-sc-111k07d-4 cGOMnI')

    lista_juegos = []
    for juego in juegos:
        n_juego = juego.find('p').text
        nn_juego = juego.find('span').text
        lista_juegos.append(n_juego.lower())
        lista_juegos.append(nn_juego.lower())
        if n_juego == 'Athens 1896':
            break

    for i, value in enumerate(lista_juegos):
        lista_juegos[i:(i+2)] = [' '.join(lista_juegos[i:(i+2)])]
    
    copia_lista_juegos = lista_juegos.copy()

    for i, value in enumerate(copia_lista_juegos):
        if 'winter' in value:
            lista_juegos.remove(value)
    
    juegos_ano = []
    for i, value in enumerate(lista_juegos):
        elem = lista_juegos[i].split(' ')
        elem.pop()
        juegos_ano.append(elem)
    
    for value in juegos_ano:
        if value[0] == 'st.':
            value[:2] = ['-'.join(value[:2])]
            value[0] = 'st-louis'
    
        elif len(value) > 2:
            value[0:len(value)-1] = ['-'.join(value[0:len(value)-1])]

    juegos_ano.pop(0) #para eliminar Tokyo
    return juegos_ano


def request_100m(juegos_ano, sex):

    '''Esta función utiliza una lista de binomios ['juegos', 'año'] para extraer cada uno de los campeones de la prueba de 100 metros en 
    función de los parámetros. Para ello, tendremos que darle como valores la lista y el sexo de los atletas en formato string('men' o 'women').
    Una vez hecho esto, lo guarda en un fichero formato CSV y retorna el dataframe obtenido.'''

    dict_100m = [] #{"Name":"__", "Country":"__", "Time":"__", "Games":"__"}

    for value in juegos_ano:
        
        URL = 'https://olympics.com/en/olympic-games/' + value[0] + '-' + value[1] + '/results/athletics/100m-' + sex
        
        r = requests.get(URL)
        soup_gold = BeautifulSoup(r.text, 'lxml')

        try:
            name = soup_gold.find(class_ = 'styles__AthleteName-sc-1yhe77y-3 edUsrV').text
        
        except:
            name = None

        try:
            country = soup_gold.find(class_ = 'styles__CountryName-sc-1r5phm6-1 ihDbcl').text
        
        except:
            country = None
        
        try:
            result = soup_gold.find(class_='styles__Info-sc-cjoz4h-0 eVxhcK').find_all('span')
            time = result[1].text

        except:
            result = None
            time = None

        dict_100m.append({'Name':name, 'Country':country, 'Time':time, 'Games':(value[0] + ' ' + value[1]), 'Year':value[1]})

    df_100m = pd.DataFrame(dict_100m)
    df_100m.to_csv('./data/100m/100m_' + sex + '.csv', index = False)
    
    return df_100m

def df_clean(df):

    '''1. Esta función realiza la limpieza de los datos del fichero CSV de los Juegos Olímpicos. Algunos de los países venían
    con la forma "Greece-1", por lo que hubo que eliminar ese guión y ese número.
    2. Después filtra las olimpiadas de verano, ya que tenemos la información en este fichero tanto de las de verano como las
    de invierno.
    3. Combinamos la columna "Games" y "City", además de eliminar la palabra "Summer" para tener el nombre de cada uno de 
    los Juegos Olímpicos con el formato "Athina 2004".'''

    for i in range(df['Team'].shape[0]):
        if df['Team'][i][-2] == '-':
            df['Team'][i] = df['Team'][i].split('-')[0]
    
    df = df.loc[df['Season'] == 'Summer']

    df['Games'] = df['City'] + ' ' + df['Games']
    df['Games'] = df['Games'].replace({'Summer': ' '}, regex = True)
    df = df.sort_values('Year', ascending = True)

    return df


def create_trace_scatter(x_, y_, name_, mode_, marker_, marker_symbol_ = None, text_ = None):
    
    '''Mandamos todos los datos necesarios para dibujar la gráfica. Esto devolverá cada uno de los "trace" que irán junto con el "layout"
    en el momento de la representación. Las variables necesarias son:
    x_:  Valores del eje x
    y_: valores del eje y
    name_: nombre de la gráfica
    marker_: formato de la línea/punto
    marker_symbol_: None por defecto. Sirve para dar diversas formas a los puntos.
    text_: El texto que se muestra en los puntos cuando interactúas con el gráfico'''

    trace = go.Scatter(
                    x = x_,
                    y = y_,
                    name = name_,
                    mode= mode_,
                    marker = marker_,
                    marker_symbol = marker_symbol_,
                    text = text_)

    return trace


def sex_filter(df, sex):
    
    '''Filtra los atletas por categoría, en este caso Atletismo, selecciona los medallistas y los divide por sexo.'''

    df = df[df['Sport'] == 'Athletics']

    df_medals = df[df['Medal'].notna()]
    df_medals = df_medals.sort_values(['Games', 'Event'])

    df_medals_sex = df_medals.loc[df_medals['Sex'] == sex]
    return df_medals_sex


def athletes_filter(n_estudios, df, df_JJOO_):
    
    '''Filtra el dataframe para quedarnos solo con los objetos de estudio en función de la cantidad de repeticiones que introducimos
    y los almacena en una lista para realizar el filtro completo de los atletas.'''

    df_JJOO_sports = df_JJOO_.groupby(['Event'])[['Games']].nunique()
    df_sports_filtered = df_JJOO_sports.loc[df_JJOO_sports['Games'] >= n_estudios]
    lista_eventos = list(df_sports_filtered.index)

    df_filtered = df[df['Event'].isin(lista_eventos)]
    
    return df_filtered


def physical_filter(df):

    '''Filtra el dataframe que recibe por las cualidades físicas a medir, así como ordenarlos por año y evento para introducirlos 
    posteriormente en el gráfico. Devuelve un dataframe con los valores medios de cada disciplina en cada una de las ediciones.'''

    df_physical = df.groupby(['Games','Event'], sort = True, as_index=False)['Age', 'Height', 'Weight', 'Year'].mean()
    df_physical = df_physical.sort_values(['Year', 'Event'])
    return df_physical


def year_filter(df):

    '''Coge la columna donde están los Juegos y elimina los duplicados para hacer una lista con solo las ediciones. Luego eliminamos 
    la ciudad donde se celebraba para tener una lista con solo los años.'''

    year_list = (df['Games']).drop_duplicates()

    year_list = list(year_list)

    for i in range(len(year_list)):
        year_list[i] = int(''.join(n for n in year_list[i] if n.isdigit()))

    year_list.sort()
    return year_list


def year_dict(year_list, sex, rgba_list_):

    '''Crea un diccionario en el que la clave es el año de la olimpiada y el valor es el código rgba para asignarle un color a los
    puntos de la gráfica que posteriormente se va a dibujar. También devuelve la lista final de años de los Juegos Olímpicos que se
    van a estudiar.'''

    year_dict = {}
    year_list_final = []
    if sex == 'M':
        counter = 5
    elif sex == 'F':
        counter = 3
    for i in range(5):
        year_dict[year_list[counter]] = rgba_list_[i]
        year_list_final.append(year_list[counter])
        if sex == 'M':
            counter += 5
        elif sex == 'F':
            counter += 4
    return year_dict, year_list_final


def common_categories(df, year_list_final):

    '''Devuelve un dataframe con los Juegos Olímpicos que se van a estudiar, las disciplinas y los valores finales.'''

    df = df[df['Year'].isin(year_list_final)]
    df = df[~df.Event.isin(df.Event.value_counts().loc[lambda x: x < 5].index)]
    df.sort_values('Year', ascending=True)
    return df


def clean_time(df):

    '''Limpia el dataframe dado para obtener los tiempos en formato obtenidos por los campeones de cada una de las ediciones de la final de 
    los 100 Metros Lisos y los transforma en datos tipo float.'''

    df['Name'] = df['Name'].str.upper()
    df = df.sort_values('Year')
    for i in range(len(df['Time'])):
        try:
            df['Time'][i] = float(df['Time'][i])

        except:
            df['Time'][i] = df['Time'][i][:-1]
            df['Time'][i] = float(df['Time'][i])
    
    df['Time'] = df['Time'].astype(float)
    return df


def save_graph(fig, name):

    '''Guarda en el perfil de Plotly los gráficos para crear presentaciones de PowerPoint interactivas.'''

    username = 'almesa93'
    api_key = 'taYCEwhV2gPyq8yglDVB'
    chart_studio.tools.set_credentials_file(username = username, api_key = api_key)
    py.plot(fig, filename = name, auto_open = False)


def line_comparative_graph(trace1, trace2, title_, title1, title2, len1, width1):

    '''Crea un gráfico con dos escalas diferentes a cada lado, lo que permite observar de un modo adecuado
    gráficas relacionadas entre sí cuyos valores son muy dispares.'''

    fig = make_subplots(specs=[[{'secondary_y': True}]])

    fig.add_trace(trace1, secondary_y=False)
    fig.add_trace(trace2, secondary_y=True)

    fig.update_layout(
        title_text=title_)

    fig.update_yaxes(title_text=title1, secondary_y=False)
    fig.update_yaxes(title_text=title2, secondary_y=True)

    fig.update_xaxes(tickangle=45)

    fig.update_layout(width=len1, height=width1)

    iplot(fig)