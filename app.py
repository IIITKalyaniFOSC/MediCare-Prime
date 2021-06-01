from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)

def predict(values, dic):
    model = pickle.load(open('kidney.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]
    
@app.route("/")
def home():
    return render_template('kidney.html')

@app.route("/kidney", methods=['GET', 'POST'])
def kidneyPage():
    return render_template('kidney.html')

@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
    except:
        message = "Please enter valid Data"
        return render_template("kidney.html", message = message)

    return render_template('predict.html', pred = pred)

if __name__ == '__main__':
	app.run(debug = True)
