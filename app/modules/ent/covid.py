
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import pickle
import numpy as np
import pandas as pd

# Define the blueprint: 'auth', set its url prefix: app.url/auth
covid = Blueprint('covid', __name__ )

def model_predictCovid(values):
    model = pickle.load(open('../../models/covid/covid.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]

# Set the route and accepted methods
@covid.route("/heartDisease", methods=['GET', 'POST'])
def heartDisease():
    return render_template('../../templates/heartDisease.html')

@covid.route("/predictCovid", methods = ['POST', 'GET'])
def predictCovid():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictCovid(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("../../templates/index_content.html", message = message)

    return render_template('../../templates/predictCovid.html', pred = pred)   
    