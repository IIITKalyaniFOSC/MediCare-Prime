
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import pickle
import numpy as np
import pandas as pd

# Define the blueprint: 'auth', set its url prefix: app.url/auth
dengue = Blueprint('dengue', __name__ )

def model_predictDengue(values):
    model = pickle.load(open('../../models/dengue/Dengue.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]

# Set the route and accepted methods
@dengue.route("/dengue", methods=['GET', 'POST'])
def denguefun():
    return render_template('../../templates/dengue.html')

@dengue.route("/predictDengue", methods = ['POST', 'GET'])
def predictDengue():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictDengue(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("../../templates/index_content.html", message = message)

    return render_template('../../templates/predictDengue.html', pred = pred)