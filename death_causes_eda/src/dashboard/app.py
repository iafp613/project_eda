from streamlit_folium import folium_static
import streamlit as st
import pandas as pd
import geojson
import json
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import os
import sys
SEP = os.sep
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources')
import utils.dashboard_tb as dtb




path = os.path.dirname(__file__)

# Cargar las imágenes
ruta_image = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'images' + SEP
calavera = Image.open(ruta_image + 'calavera.jpg')
bandera = Image.open(ruta_image + 'bandera.png')

# Cargar los DataFrames que se van a utilizar
ruta_data = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'data' + SEP
df1 = pd.read_csv(ruta_data + 'df_tm.csv')
df2 = pd.read_csv(ruta_data + 'df_totales.csv')
df3 = pd.read_csv(ruta_data + 'df_causas.csv')
df4 = pd.read_csv(ruta_data + 'df_causas_fallecidos.csv')
df5 = pd.read_csv(ruta_data + 'df_totales_fallecidos.csv')
df6 = pd.read_csv(ruta_data + 'df_mapa.csv')


st.set_page_config(
    page_title="Spain' mortality",
    page_icon=calavera,
    layout="wide"
)
menu = st.sidebar.selectbox('Menu:',
            options=["Welcome", "Analysis and visualizations", "Tableau", "About the data", "API", "Map"])

if menu == 'Welcome':
    st.image(bandera, width=200)
    st.sidebar.markdown('### Hi, my name is *Nacho Fontal*')
    st.sidebar.markdown('This is my **first dashboard**, made in *June 3rd, 2021*')
    st.sidebar.markdown('I hope you like it and can learn from all the data offered.')
    for i in range(9): st.sidebar.write("")
    st.sidebar.markdown(f'Link to my Github account [here](https://github.com/iafp613)')
    st.sidebar.markdown(f'Link to my public Tableau [here](https://public.tableau.com/shared/42RZT5MC5?:display_count=n&:origin=viz_share_link)')
    st.sidebar.markdown(f'Link to my LinkedIn profile [here](https://www.linkedin.com/in/iafp/)')
    st.sidebar.markdown('#### *Created by:*')
    st.sidebar.markdown('##### Nacho Fontal')
    st.markdown("# **Spain' mortality**")
    st.markdown("### *From 1980 to 2019*")
    st.write('It is well known by all that in recent years the life expectancy of the Spanish population, as well\
            as the increase in the quality of care and the latest medical advances have led to a revolution in the\
            improvement of hospitals, medical centers and treatments against various diseases. On the contrary, the\
            industrialization of a large number of artisanal processes, the abusive use of chemicals in food, the\
            increase in environmental pollution, the mass exodus to cities and their stressful way of life, and\
            globalization (which spreads diseases more rapidly , as we have recently verified with SARS-CoV-2); have\
            led to an exponential growth of diseases that a few years ago were less common and an outbreak of new\
            pathologies.')
    st.write('The aim of this web application is to provide information on mortality rates in Spain as well as on their\
            causes and evolution over forty years.')

if menu == 'Analysis and visualizations':
    list0 = ['---', 'Analysis', 'Visualization']
    list1 = [
        '---',
        'Total mortality rate per year', 
        'Mortality by general causes, year and region', 
        'Mortality by specific causes, year and region' 
    ]
    list2 = [
        '---',
        'Total death rate from 1980 to 2019 in Spain',
        'Evolution of the death rate in Spain between 1980 and 2019'
    ]
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Analysis and visualizations')
    st.write("In this section you will see all the graphs about the data.")
    
    platform_0 = st.selectbox('First, choose one option', options=list0)
    if platform_0 == 'Analysis':
        st.latex(r'''\textcolor{#228B22}{\text{Specific Death Rate}}''')
        st.latex(r'''\textcolor{#F5400B}{SDR} = \frac{\textcolor{#F59B0B}{\text{Number of deaths from each cause}}}\textcolor{#F59B0B}{{\text{Total population}}}\cdot\textcolor{#F59B0B}{100}''')
        platform_1 = st.selectbox('Select data', options=list1)
        if platform_1 == 'Total mortality rate per year':
            periodo = df1['Año'].unique().tolist()
            year = st.multiselect('Select year', periodo, default=None)
            st.markdown(year)
            if st.button('Show results'):
                st.table(df1[(df1.Año.isin(year))])

        if platform_1 == 'Mortality by general causes, year and region':
            regiones = sorted(df5['CCAA'].unique().tolist())
            periodo = df5['Año'].unique().tolist()
            causa = sorted(df5['Causa de muerte'].unique().tolist())
            seleccion = st.multiselect('Select regions', regiones, default=None)
            year = st.multiselect('Select year', periodo, default=None)
            motivo = st.multiselect('Select cause', causa, default=None)
            if st.button('Show results'):
                st.write(df5[(df5.CCAA.isin(seleccion) & (df5.Año.isin(year) & (df5['Causa de muerte'].isin(motivo))))])

        if platform_1 == 'Mortality by specific causes, year and region':
            regiones = sorted(df4['CCAA'].unique().tolist())
            periodo = df4['Año'].unique().tolist()
            causa = sorted(df4['Causa de muerte'].unique().tolist())
            seleccion = st.multiselect('Select regions', regiones, default=None)
            year = st.multiselect('Select year', periodo, default=None)
            motivo = st.multiselect('Select cause', causa, default=None)
            if st.button('Show results'):
                st.write(df4[(df4.CCAA.isin(seleccion) & (df4.Año.isin(year) & (df4['Causa de muerte'].isin(motivo))))])
    
    if platform_0 == 'Visualization':
        platform_2 = st.selectbox('Choose the data you want to view', options=list2)
        if platform_2 == 'Total death rate from 1980 to 2019 in Spain':
            st.sidebar.markdown('## **Observations:**')
            st.sidebar.markdown('As you can see in this graph, the *lowest mortality rates* are between 1980 and 1982,\
                                and the *highest* you can see them in the years 1999, 2003, 2017 and 2018.')
            # region_name = st.selectbox('Select a Region', options=df1.CCAA.unique())
            fig = plt.figure(dpi=100, figsize=(10,7))
            ax = fig.gca()
            sns.barplot(x=df1['TME'], y=df1['Año'], ax=ax, orient="h")
            ax.set_ylabel("Año")
            ax.set_xlabel("TME %")
            ax.set_xlim(xmin=14.5, xmax=18.0)
            ax.set_title("Tasa de mortalidad en España de 1980 a 2019")
            st.pyplot()

        if platform_2 == 'Evolution of the death rate in Spain between 1980 and 2019':
            st.sidebar.markdown('## **Observations:**')
            st.sidebar.markdown('As you can see, the *linear regression* shows a clear positive trend.\
                Therefore, it can be deduced that over the years, the mortality rate has been ***increasing***.')
            fig = plt.figure(dpi=100, figsize=(10,6))
            ax = fig.gca()
            sns.lineplot(x="Año", y="TME", data=df1, ax=ax)
            ax.set_ylabel("Año")
            ax.set_xlabel("TME %")
            ax.set_title("Evolución de la Tasa de mortalidad total en España entre 1980 y 2019")
            st.pyplot()
            for i in range(5): st.write("")
            fig = plt.figure(dpi=100, figsize=(10,6))
            ax = fig.gca()
            sns.regplot(x=df1["Año"], y=df1["TME"], line_kws={"color":"r","alpha":0.7,"lw":5})
            ax.set_ylabel("Año")
            ax.set_xlabel("TME %")
            ax.set_title("Regresión lineal de la Tasa de mortalidad en España entre 1980 y 2019");
            st.pyplot()

if menu == 'Tableau':
    dtb.tableau()


if menu == "About the data":
    st.title('About the data...')
    st.sidebar.markdown(
        '''
        ### Original information source
        All the data sets that you can see here have been cleaned, grouped, sorted and filtered. 
        You can consult the original data on the website of the National Institute of Statistics of Spain [(INE)]
        (https://www.ine.es/index.htm) and can be downloaded:
        - Original data set for deaths in Spain: [Deaths] (https://www.ine.es/jaxiT3/Tabla.htm?t=10803)
        - Original data set for the population in Spain: [Population] (https://www.ine.es/jaxiT3/Tabla.htm?t=10262)

        '''
    )
    st.write("In this section you will see the data sets that have been used to make the graphs.")
    st.write('You can select the DataFrame you want:')
    lista = [
        'Select an option',
        'Mortality by specific causes, year and region', 
        'Mortality by general causes, year and region', 
        'Total mortality rate per year'
    ]
    platform_name = st.selectbox('Select Data', options=lista)

    if st.button('Show as DataFrame'):
        if platform_name == 'Select an option':
            for i in range(2): st.write("")
            st.markdown('***Please, select an option***')
        elif platform_name == 'Mortality by specific causes, year and region':
            for i in range(3): st.write("")
            st.write(df3)
        elif platform_name == 'Mortality by general causes, year and region':
            for i in range(3): st.write("")
            st.write(df2)
        elif platform_name == 'Total mortality rate per year':
            for i in range(3): st.write("")
            st.write(df1)

    if st.button('Show as Table'):
        if platform_name == 'Select an option':
            for i in range(2): st.write("")
            st.markdown('***Please, select an option***')
        elif platform_name == 'Mortality by specific causes, year and region':
            for i in range(3): st.write("")
            st.table(df3)
        elif platform_name == 'Mortality by general causes, year and region':
            for i in range(3): st.write("")
            st.table(df2)
        elif platform_name == 'Total mortality rate per year':
            for i in range(3): st.write("")
            st.table(df1)
    

if menu == 'API':
    st.markdown('## Here you can view the original data, after cleaning it.')
    st.markdown('#### Only people authorized by the admin can access this section')
    user_input = st.text_input('Please, write the password', type='password')
    password_file = os.path.dirname(os.path.dirname(__file__)) + SEP + 'api' + SEP + 'password.json'
    with open(password_file, "r") as json_pass_readed:
        json_password = json.load(json_pass_readed)
    if st.button('Login'):
        if user_input == json_password['password']:
            st.success('Logged in as accredited person')
            st.balloons()
            try:
                x = pd.read_json('http://localhost:6060/get/df?tok=' + user_input)
                st.write(x)
            except:
                st.warning('Admin must initialize the API first.')
        else:
            st.warning('Wrong password. Try again')
    

if menu == "Map":
    st.markdown('# Mortality distribution map in Spain')
    st.markdown('### from 1980 to 2019')
    lista3=[

    ]
    year1 = st.sidebar.slider(label = 'Año', min_value = 1980,
                            max_value = 2019 ,
                            value = 2019,
                            step = 1)
    # Abrir el geojson
    with open(ruta_data + 'spain-communities.geojson') as f:
        communities_geo = geojson.load(f)

    # Creación del plano
    communities_map = folium.Map(location=[40.207472, -3.715054], zoom_start=6, tiles='stamenwatercolor')

    # Añadir adornos
    tiles = ['stamenwatercolor','cartodbpositron','openstreetmap','stamenterrain']
    for tile in tiles:
        folium.TileLayer(tile).add_to(communities_map)

    # Generar el mapa choropleth
    choropleth = folium.Choropleth(
        geo_data=communities_geo,
        data=df6,
        columns=['CCAA', str(year1)],
        key_on='feature.properties.name',
        fill_color='YlGnBu', 
        fill_opacity=0.7, 
        line_opacity=0.6,
        legend_name='Mortality rate %',
        highlight=True).add_to(communities_map)

    # Añadir capa indicando el nombre de la comunidad
    style_function = "font-size: 15px; font-weight: bold"
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['name'], style=style_function, labels=False))

    # Crear la capa control
    folium.LayerControl().add_to(communities_map)

    # Mostrar el mapa
    folium_static(communities_map)