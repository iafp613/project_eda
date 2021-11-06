<h1 align="center"> Mortalidad en España (de 1980 a 2019) - Proyecto individual de análisis exploratorio de datos.</h1>
<p align="center"><img src="https://2.bp.blogspot.com/-EGspiXUOIHU/V45NH58rCII/AAAAAAAAAlE/5EEvO7A-WhYILmWhV5FBBFPxrlW9na0CwCLcB/s1600/final.jpg"/></p>

_Es bien sabido por todos que en los últimos años, la esperanza de vida de la población española, así como el aumento de la calidad asistencial y los últimos avances médicos han supuesto una revolución en la mejora de hospitales, centros médicos y tratamientos frente a diversas enfermedades. Por el contrario, la industrialización de un gran número de procesos artesanales, el uso abusivo de químicos en los alimentos, el aumento de la contaminación ambiental, el éxodo masivo a las ciudades y su estresante modo de vida, y la globalización (que propaga enfermedades más rápidamente, como hemos verificado recientemente con SARS-CoV-2); han provocado un crecimiento exponencial de enfermedades (que hace unos años eran menos frecuentes) y un brote de nuevas patologías._

_Por este motivo, quise realizar un análisis exploratorio de datos para comprobar si las tasas de mortalidad en España han aumentado o, por el contrario, han disminuido._

_Con todos los datos obtenidos quiero concluir si en España, la tecnología, los avances médicos y el estilo de vida de los últimos cuarenta años han contribuido o no al aumento de la mortalidad._

![GitHub watchers](https://img.shields.io/github/watchers/iafp613/project_eda?style=social)


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo, pruebas o visualización._

Dentro de la carpeta `src` están contenidos todos los archivos ejecutables. El notebook principal es `main`, el cual contiene toda la información del proceso de limpieza y visualización de datos. 

Dentro de `utils`, los archivos `folders_tb.py`, `visualization_tb.py` y `mining_data_tb.py` contienen las funcionalidades que se importan en el notebook principal. El archivo `dashboard_tb.py`contiene las funcionalidades para ejecutar el dashboard y el archivo `api_tb` las necesarias para ejecutar la API.

En la carpeta `dashboard` encontramos `app.py` y todo el código necesario para poder ver el trabajo mediante Streamlit.

En la carpeta `api` hay un archivo `server.py` que contiene el código para ejecutar una API que nos retornará un *json* con todos los datos limpios. Para ejecutar la API desde la consola o desde el menú de Streamlit, se requieren dos contraseñas que no se han subido al repositorio (por seguridad). Así que, aunque el código es visible, no se podrá ejecutar.

Si nos vamos a la carpeta `data`, podemos acceder a todos los archivos .csv (brutos y limpios) que se han utilizado en este proyecto. Y en `resources` encontraremos copias de las gráficas, imágenes y datos definitivos utilizados.


### Pre-requisitos 📋

_Para poder ejecutar el código entero, necesitarás tener instaladas una serie de librerías (así como Python v.3.7.4). Todas las librerías que se han usado son:_

```
os 
sys
pandas 
re 
pyplot
csv
seaborn
pyecharts
json
flask
argparse
streamlit 
geojson 
PIL
folium
```


### Instalación 🔧

**Recuerda:**

*En la terminal del sistema operativo:*

```
pip3 install pandas
```

```
pip3 install folium
```
*Etc.*


## Construido con 🛠️

* [VSC](https://code.visualstudio.com/download) - Editor de código
* [Public Tableau](https://public.tableau.com/s/) - Dashboard interactivo
* [Prezi](https://www.prezi.com/) - Usado para la presentación del proyecto


![Your Repository's Stats](https://github-readme-stats.vercel.app/api/top-langs/?username=iafp613&theme=blue-green)


## Contribuyendo 🖇️

*Por favor, déjame una estrella en mi perfil y/o hazme un follow, ayudas a seguir subiendo más contenido.* 😊

![GitHub followers](https://img.shields.io/github/followers/iafp613?style=social)
![GitHub User's stars](https://img.shields.io/github/stars/iafp613?style=social)
![GitHub forks](https://img.shields.io/github/forks/iafp613/projects_tb?style=social)


## Más recursos 📌

[Public Tableau](https://public.tableau.com/shared/8BWKPRF8S?:display_count=n&:origin=viz_share_link) - Gráficas en Tableau


## Autor ✒️

* **Nacho Fontal** - *Proyecto* - [![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/iafp/)


## Licencia 📄

Este proyecto está bajo la Licencia (mira el archivo [LICENSE.md](LICENSE.md) para detalles).


## Expresiones de Gratitud 🎁

Muchísimas gracias a todo el equipo de The Bridge School y, en especial, a mis profesores:
* *Gabriel Vázquez Torres, Clara Piniella Marínez y Borja Puig de la Bellacasa* 📢 
* Porque gracias a vosotros y a vuestra paciencia, en menos de dos meses, he aprendido muchísimo 🤓.
* ¡Os debo una cerveza 🍺 o un café ☕! ¡Gracias de corazón!
---