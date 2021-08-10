import matplotlib.pyplot as plt
import os

def guardar_df(df, name):
    '''Guarda el DataFrame en la carpeta de datos del dashboard (en formato .csv).
    Hay que añadirle el nombre con el que queremos guardarlo (terminado en '.csv')

    Parámetros:
    df ---> Nombre del DataFrame que queremos guardar.
    name ---> Nombre con el que queremos guardarlo (.csv)

    '''
    SEP = os.sep
    ruta = os.path.dirname(os.getcwd()) + SEP + 'resources' + SEP + 'data' + SEP
    df.to_csv(ruta + name, index=False)

def guardar_grafico(name):
    SEP = os.sep
    ruta = os.path.dirname(os.getcwd()) + SEP + 'resources' + SEP + 'graphics' + SEP
    plt.savefig(ruta + name)