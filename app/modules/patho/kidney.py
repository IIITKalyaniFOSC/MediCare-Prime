
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import pickle
import numpy as np
import pandas as pd

# Define the blueprint: 'auth', set its url prefix: app.url/auth
kidney = Blueprint('kidney', __name__ )

def model_predictKidney(values):
    model = pickle.load(open('../../models/kidney/kidney.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0] 

# Set the route and accepted methods
@kidney.route("/kidney", methods=['GET', 'POST'])
def kidneyfun():
    return render_template('../../templates/kidney.html')

@kidney.route("/predictKidney", methods = ['POST', 'GET'])
def predictKidney():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictKidney(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("../../templates/index_content.html", message = message)

    return render_template('../templates/predictKidney.html', pred = pred)