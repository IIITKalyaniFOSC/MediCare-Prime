
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import pickle
import numpy as np
import pandas as pd

# Define the blueprint: 'auth', set its url prefix: app.url/auth
diabetes = Blueprint('diabetes', __name__ )

def model_predictDiabetes(values):
    model = pickle.load(open('../../models/diabetes/diabetes.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]

# Set the route and accepted methods
@diabetes.route("/diabetes", methods=['GET', 'POST'])
def diabetesfun():
    return render_template('../../templates/diabetes.html')

@diabetes.route("/predictDiabetes", methods = ['POST', 'GET'])
def predictDiabetes():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictDiabetes(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("../../index_content.html", message = message)

    return render_template('../../templates/predictDiabetes.html', pred = pred)