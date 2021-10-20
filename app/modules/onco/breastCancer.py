
# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
import pickle
import numpy as np
import pandas as pd

# Define the blueprint: 'auth', set its url prefix: app.url/auth
breast_cancer = Blueprint('breastcancer', __name__ )

def model_predictBreastCancer(df):
    model1 = pickle.load(open('../../models/breastCancer/model1.pickle','rb'))
    return model1.predict(df)[0]

# Set the route and accepted methods
@breast_cancer.route("/breastCancer", methods=['GET', 'POST'])
def breastCancer():
    return render_template('../../templates/breastCancer.html')   

@breast_cancer.route('/predictBreastCancer',methods=['POST'])
def predictBreastCancer():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension',
       'radius error', 'texture error', 'perimeter error', 'area error',
       'smoothness error', 'compactness error', 'concavity error',
       'concave points error', 'symmetry error', 'fractal dimension error',
       'worst radius', 'worst texture', 'worst perimeter', 'worst area',
       'worst smoothness', 'worst compactness', 'worst concavity',
       'worst concave points', 'worst symmetry', 'worst fractal dimension']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model_predictBreastCancer(df)
        
    if output[0] == 'M':
        res_val = "breast cancer "
    else:
        res_val = "no breast cancer"

    return render_template('../../templates/breastCancer.html', prediction_text='Patient has {}'.format(res_val))