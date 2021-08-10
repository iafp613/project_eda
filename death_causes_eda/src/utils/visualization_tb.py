import seaborn as sns
import matplotlib.pyplot as plt

def grafica(tipo, datos):
    try:
        fig = plt.figure(dpi=100, figsize=(8,5))
        ax = fig.gca()
        if tipo == 'lineplot':
            sns.lineplot(x="Año", y="TME", data=datos, ax=ax)
            ax.set_ylabel("Año")
            ax.set_xlabel("TME %")
            return ax.set_title("Evolución de la tasa de mortalidad total en España entre 1980 y 2019")
        if tipo == 'regplot':
            ax.set_ylabel("Año")
            ax.set_xlabel("TME %")
            ax.set_title("Regresión lineal de la tasa de mortalidad total en España entre 1980 y 2019")
            return sns.regplot(x=datos["Año"], y=datos["TME"], line_kws={"color":"r","alpha":0.7,"lw":5})
        if tipo == 'histplot':
            ax.set_ylabel("Frecuencia")
            ax.set_xlabel("TME %")
            ax.set_title("Frecuencia de aparición de las diferentes tasas de mortalidad")
            return sns.histplot(data=datos, x="TME", bins=5)
        if tipo == 'barplot':
            ax.set_ylabel("Año")
            ax.set_xlabel("TME %")
            ax.set_xlim(xmin=14.5, xmax=18.0)
            ax.set_title("Tasa de mortalidad en España de 1980 a 2019")
            return sns.barplot(x=datos['TME'], y=datos['Año'], ax=ax, orient="h")
        if tipo == 'boxplot':
            ax.set_ylabel("TME")
            ax.set_title("Outliers de la tasa de mortalidad")
            return sns.boxplot(x=datos['TME'], data=datos, color='red')
        if tipo == 'scatterplot':
            ax.set_ylabel("TME %")
            ax.set_xlabel("Año")
            ax.set_title("Scatterplot de la tasa de mortalidad en España de 1980 a 2019")
            return sns.scatterplot(data=datos, x="Año", y="TME", size='TME', hue='TME')
    except Exception as error:
        print('Ha ocurrido un error')