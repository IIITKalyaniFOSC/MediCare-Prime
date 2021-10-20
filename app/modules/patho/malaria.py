
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from werkzeug.utils import secure_filename

# Define the blueprint: 'auth', set its url prefix: app.url/auth
malaria = Blueprint('malaria', __name__ )

def model_predictMalaria(img_path):
    model = load_model('../../models/malaria/malaria.h5')
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x=x/255
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    print(preds)
    return preds

# Set the route and accepted methods
@malaria.route("/malaria", methods=['GET', 'POST'])
def malariafun():
    return render_template('../../templates/malaria.html')

@malaria.route("/predictMalaria", methods = ['POST', 'GET'])
def predictMalaria():
    output = "Invalid request method"
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, '../../static/uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predictMalaria(file_path)

        class_names =  ["The Person is Infected With Malaria.","The Person is not Infected With Malaria."]
        output = class_names[preds[0]]
      
    return render_template('../../templates/predictMalaria.html', pred = output)