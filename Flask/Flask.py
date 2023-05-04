from flask import Flask, render_template, request
import numpy as np
from skimage.io import imread 
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
import cv2 
from PIL import Image


from keras.models import Sequential
from tensorflow import keras

model = keras.models.load_model('Base_model.h5')

app = Flask(__name__)



@app.route('/') # este es el home, con la plantilla que busca en la carpeta templates (es la pagina web ya prediseñada en biblioteca)
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    IMAGE_HEIGHT = 125
    IMAGE_WIDTH = 125
    
    #TODO hay problemas para leer bmp, quizás hay que convertir a jpg con PIL
    try:
        image = request.files['imagen']    
        app.logger.debug("error",image)
        testing_image = np.array([cv2.resize(imread(image),(IMAGE_WIDTH,IMAGE_HEIGHT))/255.0])
        
        pred = model.predict(testing_image)
        return render_template('after.html', data=pred)
    
    except Exception as e:
        # Ocurrió un error desconocido
         return render_template('error.html', data={e})


if __name__ == "__main__":
    app.run(debug=True)