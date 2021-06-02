from flask import Flask, request, render_template
import pickle, os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from werkzeug.utils import secure_filename

app = Flask(__name__)

def model_predictKidney(values):
    model = pickle.load(open('models/kidney/kidney.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]

def model_predictDengue(values):
    model = pickle.load(open('models/dengue/dengue.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]
    
def model_predictMalaria(img_path):
    model = load_model('models/malaria/malaria.h5')
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x=x/255
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    print(preds)
    return preds
    
@app.route("/")
def home():
    return render_template('index_content.html')

@app.route("/kidney", methods=['GET', 'POST'])
def kidney():
    return render_template('kidney.html')
    
@app.route("/dengue", methods=['GET', 'POST'])
def dengue():
    return render_template('dengue.html')
    
@app.route("/malaria", methods=['GET', 'POST'])
def malaria():
    return render_template('malaria.html')

@app.route("/predictKidney", methods = ['POST', 'GET'])
def predictKidney():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictKidney(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("index_content.html", message = message)

    return render_template('predictKidney.html', pred = pred)
    
@app.route("/predictDengue", methods = ['POST', 'GET'])
def predictDengue():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictKidney(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("index_content.html", message = message)

    return render_template('predictDengue.html', pred = pred)
    
@app.route("/predictMalaria", methods = ['POST', 'GET'])
def predictMalaria():
    output = "Invalid request method"
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'static/uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predictMalaria(file_path)

        class_names =  ["The Person is Infected With Malaria.","The Person is not Infected With Malaria."]
        output = class_names[preds[0]]
      
    return render_template('predictMalaria.html', pred = output)

if __name__ == '__main__':
	app.run(debug = True)
