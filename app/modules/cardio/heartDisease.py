
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import pickle
import numpy as np
import pandas as pd

# Define the blueprint: 'auth', set its url prefix: app.url/auth
heart_disease = Blueprint('heartdisease', __name__ )

def model_predictHeartDisease(df):
    model = pickle.load(open('../../models/heartDisease/model.pickle','rb'))
    return model.predict(df)[0]

# Set the route and accepted methods
@heart_disease.route("/heartDisease", methods=['GET', 'POST'])
def heartDisease():
    return render_template('../../templates/heartDisease.html')

@heart_disease.route('/predictHeartDisease',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model_predictHeartDisease(df)
        
    if output == 1:
        res_val = "Heart Disease"
    else:
        res_val = "no Heart Disease."
        

    return render_template('../../templates/heartDisease.html', prediction_text='Patient has {}'.format(res_val))     
    