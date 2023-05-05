# <div align="center">**DESARROLLO FLASK**</div> 

A continuación se describirán los pasos a seguir para la creación de la parte de Flask dentro del proyecto. El objetivo de la parte de Flask es la de crear un entorno virtual en local Host en forma de página web. Allí haremos la preddicción de si la celula cargada es normal o atípica gracias a nuestro modelo de Machine Learning entrenado previamente.

Para ello necesitamos la estructura virtual en formato html que llamaremos "plantillas" o "templates", el modelo que haga las predicciones ya entrenado previamente, las imágenes a predecir y el código en un archivo .py para que encadene todo los eslabones.

<br></br>
1. [Plantillas](#id1)
2. [Código Flask.py](#id2)
3. [Imàgenes](#id3)
4. [Modelo ML](#id4)
5. [Proceso para visualizar en local host](#id5)
<br></br>

<div id='id1'/>
<h2>1. Plantillas</h2>

La estructura virtual constará de tres plantillas en formato HTML: Home, After y Error.

Home: Aquí estará el boton de "Cargar imágen" y el botón de "Predecir". Además ponemos una breve introducción y un aspecto más agradable a la vista.

After: Será el resultado de la predicción siendo "Normal" o "Atípica" en función del resultado que nos da el modelo. Resultado cercano a 0 es "Normal" y cercano a "1" para Atípica.
 
Error: En caso de que diera algún error al cargar la foto (formato indebido, otro tipo de documento, etc.) en lugar de un pantallazo de error, vuelva a la página home.

<div id='id2'/>
<h2> 2. Código Flask.py</h2>

Aquí crearemos las rutas  de un código para Flask. Empezamos creando la APP y cargando el modelo de Machine Learning.

Ruta Home (/). Se cargara la plantilla "home" de la carpeta "Template".
    Las imágenes a cargar para la visualización deben estar en formato .JPG para evitar errores. Se encuentran en la carpeta "static". Asegurarse de llamar correctamente a las fotos en la ruta.
    
Ruta Predict (/Predict). Con método "Post" para subir la imagen (request.file), y previo pretratamiento de la imagen (cv.resize), hará la predicción (model.predict).

En caso de Error, metemos el template "Error" ya descrito anteriormente.

<div id='id3'/>
<h2> 3. Imàgenes</h2>

Las imágenes a cargar deben estar en formato .JPG para evitar errores. Se encuentran en la carpeta "static". Asegurarse de llamar correctamente a las fotos

<div id='id4'/>
<h2> 4. Modelo ML</h2>

El modelo está en formato .h5, el cual ha sido el resultado de un proyecto de Machine Learning: (https://github.com/marinagoju/CNN_Cervical_Cancer).

<div id='id5'/>
<h2> 5. Proceso para visualizar en local host</h2>

Para la visualización de "Home" se le debe dar a ejecutar en flask.py y luego meternos en la IP Local Host que nos proporciona la biblioteca Flask en la terminar abierta previamente.
Por ejemplo: "* Running on http://127.0.0.1:5000". Esta dirección será la URL de pongamos en nuestro navegador.
Asegurate de estar en el directorio de la carpeta para que no te de error.
