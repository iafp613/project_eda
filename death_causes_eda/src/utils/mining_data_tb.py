import csv
import re

cambios = {
    '001102  IXXIITodas las causas': 'Todas las causas', 
    '001008  IEnfermedades infecciosas y parasitarias': 'Todas las enfermedades infecciosas y parasitarias', 
    '001  Enfermedades infecciosas intestinales': 'Enfermedades infecciosas intestinales', 
    '002  Tuberculosis y sus efectos tard�os': 'Tuberculosis y sus efectos tardíos', 
    '003  Enfermedad meningoc�cica': 'Enfermedad meningocócica', 
    '004  Septicemia': 'Septicemia', 
    '005  Hepatitis v�rica': 'Hepatitis vírica', 
    '006  SIDA': 'SIDA', 
    '007  VIH+ (portador, evidencias de laboratorio del VIH, )': 'VIH+', 
    '008  Resto de enfermedades infecciosas y parasitarias y sus efectos tard�os': 'Resto de enfermedades infecciosas y parasitarias y sus efectos tardíos', 
    '009041  IITumores': 'Todos los tumores', 
    '009  Tumor maligno del labio, de la cavidad bucal y de la faringe': 'Tumor maligno del labio, de la cavidad bucal y de la faringe', 
    '010  Tumor maligno del es�fago': 'Tumor maligno del esófago', 
    '011  Tumor maligno del est�mago': 'Tumor maligno del estómago', 
    '012  Tumor maligno del colon': 'Tumor maligno del colon', 
    '013  Tumor maligno del recto, de la porci�n rectosigmoide y del ano': 'Tumor maligno del recto, de la porción rectosigmoide y del ano', 
    '014  Tumor maligno del h�gado y v�as biliares intrahep�ticas': 'Tumor maligno del hígado y vías biliares intrahepáticas', 
    '015  Tumor maligno del p�ncreas': 'Tumor maligno del páncreas', 
    '016  Otros tumores malignos digestivos': 'Otros tumores malignos digestivos', 
    '017  Tumor maligno de la laringe': 'Tumor maligno de la laringe', 
    '018  Tumor maligno de la tr�quea, de los bronquios y del pulm�n': 'Tumor maligno de la tráquea, bronquios y pulmón',
    '019  Otros tumores malignos respiratorios e intrator�cicos': 'Otros tumores malignos respiratorios e intratorácicos', 
    '020  Tumores malignos del hueso y de los cart�lagos articulares': 'Tumores malignos del hueso y de los cartílagos articulares', 
    '021  Melanoma maligno de la piel': 'Melanoma maligno de la piel', 
    '022  Otros tumores malignos de la piel y de los tejidos blandos': 'Otros tumores malignos de la piel y de los tejidos blandos', 
    '023  Tumor maligno de la mama': 'Tumor maligno de la mama', 
    '024  Tumor maligno del cuello del �tero': 'Tumor maligno del cuello del útero', 
    '025  Tumor maligno de otras partes del �tero': 'Tumor maligno de otras partes del útero', 
    '026  Tumor maligno del ovario': 'Tumor maligno del ovario', 
    '027  Tumores malignos de otros �rganos genitales femeninos': 'Tumores malignos de otros órganos genitales femeninos', 
    '028  Tumor maligno de la pr�stata': 'Tumor maligno de la próstata', 
    '029  Tumores malignos de otros �rganos genitales masculinos': 'Tumores malignos de otros órganos genitales masculinos', 
    '030  Tumor maligno del ri��n, excepto pelvis renal': 'Tumor maligno del riñón', 
    '031  Tumor maligno de la vejiga': 'Tumor maligno de la vejiga', 
    '032  Otros tumores malignos de las v�as urinarias': 'Otros tumores malignos de las vías urinarias', 
    '033  Tumor maligno del enc�falo': 'Tumor maligno del encéfalo', 
    '034  Otros tumores malignos neurol�gicos y endocrinos': 'Otros tumores malignos neurológicos y endocrinos', 
    '035  Tumor maligno de sitios mal definidos, secundarios y de sitios no especificados': 'Tumor maligno de sitios mal definidos', 
    '036  Tumores malignos del tejido linf�tico, de los �rganos hematopoy�ticos y de tejidos afines, excepto leucemia': 'Tumores malignos del tejido linfático, de los órganos hematopoyéticos y de tejidos afines, excepto leucemia', 
    '037  Leucemia': 'Leucemia', 
    '038  Tumores in situ': 'Tumores in situ', 
    '039  Tumores benignos': 'Tumores benignos', 
    '040  S�ndrome mielodispl�sico': 'Síndrome mielodisplásico', 
    '041  Otros tumores de comportamiento incierto o desconocido': 'Otros tumores de comportamiento incierto o desconocido', 
    '042043  IIIEnfermedades de la sangre y de los �rganos hematopoy�ticos, y ciertos trastornos que afectan al mecanismo de la inmunidad': 'Todas las enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan al mecanismo de la inmunidad', 
    '042 Enfermedades de la sangre y de los �rganos hematopoy�ticos': 'Enfermedades de la sangre y de los órganos hematopoyéticos', 
    '043 Ciertos trastornos que afectan al mecanismo de la inmunidad': 'Ciertos trastornos que afectan al mecanismo de la inmunidad', 
    '044045  IVEnfermedades endocrinas, nutricionales y metab�licas': 'Todas las enfermedades endocrinas, nutricionales y metabólicas', 
    '044  Diabetes mellitus': 'Diabetes mellitus', 
    '045  Otras enfermedades endocrinas, nutricionales y metab�licas': 'Otras enfermedades endocrinas, nutricionales y metabólicas', 
    '046049  VTrastornos mentales y del comportamiento': 'Todos los trastornos mentales y del comportamiento', 
    '046  Trastornos mentales org�nicos, senil y presenil': 'Trastornos mentales orgánicos, senil y presenil', 
    '047  Trastornos mentales debidos al uso de alcohol': 'Trastornos mentales debidos al uso de alcohol', 
    '048  Trastornos mentales debidos al uso de drogas (drogodependencia, toxicoman�a)': 'Trastornos mentales debidos al uso de drogas (drogodependencia, toxicomanía)', 
    '049  Otros trastornos mentales y del comportamiento': 'Otros trastornos mentales y del comportamiento', 
    '050052  VIVIIIEnfermedades del sistema nervioso y de los �rganos de los sentidos': 'Todas las enfermedades del sistema nervioso y de los órganos de los sentidos', 
    '050  Meningitis (otras en 003)': 'Otras meningitis', 
    '051  Enfermedad de Alzheimer': 'Alzheimer', 
    '052  Otras enfermedades del sistema nervioso y de los �rganos de los sentidos': 'Otras enfermedades del sistema nervioso y de los órganos de los sentidos', 
    '053061 IXEnfermedades del sistema circulatorio': 'Todas las enfermedades del sistema circulatorio', 
    '053  Enfermedades card�acas reum�ticas cr�nicas': 'Enfermedades cardíacas reumáticas crónicas', 
    '054  Enfermedades hipertensivas': 'Enfermedades hipertensivas', 
    '055  Infarto agudo de miocardio': 'Infarto agudo de miocardio', 
    '056  Otras enfermedades isqu�micas del coraz�n': 'Otras enfermedades isquémicas del corazón', 
    '057  Insuficiencia card�aca': 'Insuficiencia cardíaca', 
    '058 Otras enfermedades del coraz�n': 'Otras enfermedades del corazón', 
    '059  Enfermedades cerebrovasculares': 'Enfermedades cerebrovasculares', 
    '060  Aterosclerosis': 'Aterosclerosis', 
    '061  Otras enfermedades de los vasos sangu�neos': 'Otras enfermedades de los vasos sanguíneos', 
    '062067  XEnfermedades del sistema respiratorio': 'Todas las enfermedades del sistema respiratorio', 
    '062  Influenza (gripe) (incluye gripe aviar y gripe A)': 'Influenza (gripe, incluye gripe aviar y gripe A)', 
    '063  Neumon�a': 'Neumonía', 
    '064  Enfermedades cr�nicas de las v�as respiratorias inferiores (excepto asma)': 'Enfermedades crónicas de las vías respiratorias inferiores (excepto asma)', 
    '065  Asma': 'Asma', 
    '066  Insuficiencia respiratoria': 'Insuficiencia respiratoria', 
    '067  Otras enfermedades del sistema respiratorio': 'Otras enfermedades del sistema respiratorio', 
    '068072  XIEnfermedades del sistema digestivo': 'Todas las enfermedades del sistema digestivo', 
    '068  �lcera de est�mago, duodeno y yeyuno': 'Úlcera de estómago, duodeno y yeyuno', 
    '069  Enteritis y colitis no infecciosas': 'Enteritis y colitis no infecciosas', 
    '070  Enfermedad vascular intestinal': 'Enfermedad vascular intestinal', 
    '071  Cirrosis y otras enfermedades cr�nicas del h�gado': 'Cirrosis y otras enfermedades crónicas del hígado', 
    '072  Otras enfermedades del sistema digestivo': 'Otras enfermedades del sistema digestivo', 
    '073  XIIEnfermedades de la piel y del tejido subcut�neo': 'Todas las enfermedades de la piel y del tejido subcutáneo', 
    '074076  XIIIEnfermedades del sistema osteomuscular y del tejido conjuntivo': 'Todas las enfermedades del sistema osteomuscular y del tejido conjuntivo', 
    '074  Artritis reumatoide y osteoartrosis': 'Artritis reumatoide y osteoartrosis', 
    '075  Osteoporosis y fractura patol�gica': 'Osteoporosis y fractura patológica', 
    '076  Otras enfermedades del sistema osteomuscular y del tejido conjuntivo': 'Otras enfermedades del sistema osteomuscular y del tejido conjuntivo', 
    '077080  XIVEnfermedades del sistema genitourinario': 'Todas las enfermedades del sistema genitourinario', 
    '077  Enfermedades del ri��n y del ur�ter': 'Enfermedades del riñón y del uréter', 
    '078  Enfermedades de los �rganos genitales masculinos': 'Enfermedades de los órganos genitales masculinos', 
    '079  Enfermedades de los �rganos genitales femeninos y trastornos de la mama': 'Enfermedades de los órganos genitales femeninos y trastornos de la mama', 
    '080  Otras enfermedades del sistema genitourinario': 'Otras enfermedades del sistema genitourinario', 
    '081  XVEmbarazo, parto y puerperio': 'Todos los fallecimientos a causa del embarazo, parto o puerperio', 
    '082  XVIAfecciones originadas en el periodo perinatal': 'Todas las afecciones originadas en el periodo perinatal', 
    '083085  XVIIMalformaciones cong�nitas, deformidades y anomal�as cromos�micas': 'Todas las malformaciones congénitas, deformidades y anomalías cromosómicas', 
    '083  Malformaciones cong�nitas del sistema nervioso': 'Malformaciones congénitas del sistema nervioso', 
    '084  Malformaciones cong�nitas del sistema circulatorio': 'Malformaciones congénitas del sistema circulatorio', 
    '085  Otras malformaciones cong�nitas, deformidades y anomal�as cromos�micas': 'Otras malformaciones congénitas, deformidades y anomalías cromosómicas', 
    '086089  XVIIIS�ntomas, signos y hallazgos anormales cl�nicos y de laboratorio, no clasificados en otra parte': 'Todos los síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte', 
    '086 Paro card�aco, muerte sin asistencia y otra causa desconocida de mortalidad': 'Paro cardíaco, muerte sin asistencia y otra causa desconocida de mortalidad', 
    '087  Senilidad': 'Senilidad', 
    '088 Muerte s�bita infantil': 'Muerte súbita infantil', 
    '089  Resto de s�ntomas, signos y hallazgos anormales cl�nicos y de laboratorio, no clasificados en otra parte': 'Resto de síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte', 
    '090102  XXCausas externas de mortalidad': 'Todas las causas externas de mortalidad', 
    '090  Accidentes de tr�fico': 'Accidentes de tráfico', 
    '091  Otros accidentes de transporte': 'Otros accidentes de transporte', 
    '092  Ca�das accidentales': 'Caídas accidentales', 
    '093  Ahogamiento, sumersi�n y sofocaci�n accidentales': 'Ahogamiento, sumersión y sofocación accidentales', 
    '094  Accidentes por fuego, humo y sustancias calientes': 'Accidentes por fuego, humo y sustancias calientes', 
    '095  Envenenamiento accidental por psicof�rmacos y drogas de abuso': 'Envenenamiento accidental por psicofármacos y drogas de abuso', 
    '096  Otros envenenamientos accidentales': 'Otros envenenamientos accidentales', 
    '097  Otros accidentes': 'Otros accidentes', 
    '098  Suicidio y lesiones autoinfligidas': 'Suicidio y lesiones autoinfligidas', 
    '099  Agresiones (homicidio)': 'Agresiones (homicidio)', 
    '100  Eventos de intenci�n no determinada': 'Eventos de intención no determinada', 
    '101  Complicaciones de la atenci�n m�dica y quir�rgica': 'Complicaciones de la atención médica y quirúrgica', 
    '102  Otras causas externas y sus efectos tard�os': 'Otras causas externas y sus efectos tardíos', 
    'Total': 'Ambos', 
    'Todas las edades': 'Todas', 
    '01 Andaluc�a': 'Andalucía', 
    '02 Arag�n': 'Aragón', 
    '03 Asturias, Principado de': 'Asturias', 
    '04 Balears, Illes': 'Baleares', 
    '05 Canarias': 'Canarias', 
    '06 Cantabria': 'Cantabria', 
    '07 Castilla y Le�n': 'Castilla y León', 
    '08 Castilla - La Mancha': 'Castilla La Mancha', 
    '08 Castilla  La Mancha': 'Castilla La Mancha', 
    '09 Catalu�a': 'Cataluña', 
    '10 Comunitat Valenciana': 'Comunidad Valenciana', 
    '11 Extremadura': 'Extremadura', 
    '12 Galicia': 'Galicia', 
    '13 Madrid, Comunidad de': 'Madrid', 
    '14 Murcia, Regi�n de': 'Murcia', 
    '15 Navarra, Comunidad Foral de': 'Navarra', 
    '16 Pa�s Vasco': 'País Vasco', 
    '17 Rioja, La': 'La Rioja', 
    '18 Ceuta': 'Ceuta', 
    '19 Melilla': 'Melilla', 
}

years = {
    '1 de enero de 2019': 2019, 
    '1 de enero de 2018': 2018, 
    '1 de enero de 2017': 2017, 
    '1 de enero de 2016': 2016, 
    '1 de enero de 2015': 2015, 
    '1 de enero de 2014': 2014, 
    '1 de enero de 2013': 2013, 
    '1 de enero de 2012': 2012, 
    '1 de enero de 2011': 2011, 
    '1 de enero de 2010': 2010, 
    '1 de enero de 2009': 2009, 
    '1 de enero de 2008': 2008, 
    '1 de enero de 2007': 2007, 
    '1 de enero de 2006': 2006, 
    '1 de enero de 2005': 2005, 
    '1 de enero de 2004': 2004, 
    '1 de enero de 2003': 2003, 
    '1 de enero de 2002': 2002, 
    '1 de enero de 2001': 2001, 
    '1 de enero de 2000': 2000, 
    '1 de enero de 1999': 1999, 
    '1 de enero de 1998': 1998, 
    '1 de enero de 1997': 1997, 
    '1 de enero de 1996': 1996, 
    '1 de enero de 1995': 1995, 
    '1 de enero de 1994': 1994, 
    '1 de enero de 1993': 1993, 
    '1 de enero de 1992': 1992, 
    '1 de enero de 1991': 1991, 
    '1 de enero de 1990': 1990, 
    '1 de enero de 1989': 1989, 
    '1 de enero de 1988': 1988, 
    '1 de enero de 1987': 1987, 
    '1 de enero de 1986': 1986, 
    '1 de enero de 1985': 1985, 
    '1 de enero de 1984': 1984, 
    '1 de enero de 1983': 1983, 
    '1 de enero de 1982': 1982, 
    '1 de enero de 1981': 1981, 
    '1 de enero de 1980': 1980, 
}



lista_redundantes = [
    'Todas las causas', 'Todas las enfermedades infecciosas y parasitarias', 'Todos los tumores', \
    'Todas las enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan al mecanismo de la inmunidad', \
    'Todas las enfermedades endocrinas, nutricionales y metabólicas', 'Todos los trastornos mentales y del comportamiento', \
    'Todas las enfermedades del sistema nervioso y de los órganos de los sentidos', \
    'Todas las enfermedades del sistema circulatorio', 'Todas las enfermedades del sistema respiratorio', \
    'Todas las enfermedades del sistema digestivo', 'Todas las enfermedades del sistema osteomuscular y del tejido conjuntivo', \
    'Todas las enfermedades del sistema genitourinario', 'Todas las malformaciones congénitas, deformidades y anomalías cromosómicas', \
    'Todos los síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte', \
    'Todas las causas externas de mortalidad'
]



lista_todas = [
    'Todas las causas', 'Todas las enfermedades infecciosas y parasitarias', 'Todos los tumores', \
    'Todas las enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan al mecanismo de la inmunidad', \
    'Todas las enfermedades endocrinas, nutricionales y metabólicas', 'Todos los trastornos mentales y del comportamiento',\
    'Todas las enfermedades del sistema nervioso y de los órganos de los sentidos', \
    'Todas las enfermedades del sistema circulatorio', 'Todas las enfermedades del sistema respiratorio', \
    'Todas las enfermedades del sistema digestivo', 'Todas las enfermedades de la piel y del tejido subcutáneo', \
    'Todas las enfermedades del sistema osteomuscular y del tejido conjuntivo', \
    'Todas las enfermedades del sistema genitourinario', 'Todos los fallecimientos a causa del embarazo, parto o puerperio', \
    'Todas las afecciones originadas en el periodo perinatal', 'Todas las malformaciones congénitas, deformidades y anomalías cromosómicas', \
    'Todos los síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte', \
    'Todas las causas externas de mortalidad'
]



def quitarpuntos(archivo):
    '''Elimina los '.' y '-' de un archivo.
    Devuelve el mismo archivo pero sin los '.' ni '-'

    Parámetros:
    archivo ---> archivo que queremos modificar.

    '''
    archivo = re.sub('[\.-]','', archivo)
    return archivo



def limpiar_def():
    '''Limpia los csv de defunciones aplicando la función quitarpuntos().
    Crea una copia limpia de cada csv.
    
    '''
    contador = 40
    numero = 1980
    for i in range(contador):
        with open(f'../data/raw/defunciones{numero}.csv', 'r') as file:
            final_data = [[quitarpuntos(str(col)) for col in line] for line in csv.reader(file)]
        with open(f'../data/clean/defunciones{numero}.csv', 'w') as file:
            csv.writer(file).writerows(final_data)
        numero +=1


def limpiar_pob():
    '''Limpia los csv de poblaciones aplicando la función quitarpuntos().
    Crea una copia limpia de cada csv.

    '''
    contador = 40
    numero = 1980
    for i in range(contador):
        with open(f'../data/raw/Poblacion{numero}.csv', 'r') as file:
            final_data = [[quitarpuntos(str(col)) for col in line] for line in csv.reader(file)]
        with open(f'../data/clean/Poblacion{numero}.csv', 'w') as file:
            csv.writer(file).writerows(final_data)
        numero +=1



def aplicar_cambios_def(lista):
    '''Cambia los valores defectuosos o imprecisos por otros nuevos.
    Aplica los cambios a todos los DataFrames que se le pasen en una lista.
    
    Parámetros:
    lista ---> Una lista de DataFrames

    '''
    for i in lista:
        i.replace(cambios, inplace=True)
        i.drop(['Sexo', 'Edad'], axis = 'columns', inplace=True)
        i.columns = ['Causa de muerte', 'CCAA', 'Año', 'Total_defunciones']



def aplicar_cambios_pob(lista):
    '''Cambia los valores defectuosos o imprecisos por otros nuevos.
    Aplica los cambios a todos los DataFrames que se le pasen en una lista.
    
    Parámetros:
    lista ---> Una lista de DataFrames

    '''
    for i in lista:
        i.replace(cambios, inplace=True)
        i.replace(years, inplace=True)
        i.drop(['Sexo', 'Edad'], axis = 'columns', inplace=True)
        i.columns = ['CCAA', 'Año', 'Total_población']



def eliminar_filas(dataframe):
    '''Elimina las filas que cumplen los criterios especificados en los bucles.
    Aplica los cambios a cada DataFrame que se le pase por parámetro.

    Parámetros:
    dataframe ---> Hay que pasarle un DataFrame.

    '''
    for i in dataframe['Causa de muerte']:
        if i in lista_redundantes:
            indexname = dataframe[dataframe['Causa de muerte'] == i].index
            dataframe.drop(indexname, inplace=True)



def analisis_df(data):
    '''Imprime a partir de DataFrame:
    La cantidad de filas y columnas que contiene.
    La información general.
    Una breve descripción estadística de los datos.
    La cantidad de valores NaN que tiene por columna.

    Parámetros:
    data ---> Un DataFrame.

    '''
    print('-----------------------# FILAS Y COLUMNAS #-------------------------')
    print(f'Cantidad de filas: {data.shape[0]} \nCantidad de columnas: {data.shape[1]}')
    print('\n----------------------# INFORMACIÓN GENERAL #-----------------------')
    print(data.info())
    print('\n-------------------# DESCRIPCIÓN ESTADÍSTICA #----------------------')
    print(data.describe())
    print('\n---------------------# CANTIDAD VALORES NaN #-----------------------')
    print('Valores NaN por columna:','\n', data.isnull().sum())
    print('Valores NaN totales en todo el DataFrame:', data.isnull().sum().sum())