import os
SEP = os.sep
import pandas as pd
ruta = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + SEP + 'resources' + SEP + 'data' + SEP + 'df_causas_fallecidos.csv'

def preparar_datos():
    datos = pd.read_csv(ruta)
    return datos.to_json()

