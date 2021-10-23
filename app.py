from flask import Flask, request, render_template
import pickle, os
import numpy as np
import pandas as pd
from flask_pymongo import PyMongo
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from werkzeug.utils import secure_filename

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'medicare-prime'
app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@cluster0.cujsu.mongodb.net/medicare-prime?retryWrites=true&w=majority'
mongo = PyMongo(app)



def model_predictKidney(values):
    model = pickle.load(open('models/kidney/kidney.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0] 

def model_predictCovid(values):
    model = pickle.load(open('models/covid/covid.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]

def model_predictDiabetes(values):
    model = pickle.load(open('models/diabetes/diabetes.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]

def model_predictDengue(values):
    model = pickle.load(open('models/dengue/Dengue.pkl','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]
 
def model_predictParkinsonDisease(values):
    model = pickle.load(open('models/ParkinsonDisease/parkinson.pickle','rb'))
    values = np.asarray(values)
    return model.predict(values.reshape(1, -1))[0]

def model_predictThyroidDisease(values):
    model = pickle.load(open('models/ThyroidDisease/thyroid.pickle','rb'))
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


def model_predictBreastCancer(df):
    model1 = pickle.load(open('models/breastCancer/model1.pickle','rb'))
    return model1.predict(df)[0]


def model_predictHeartDisease(df):
    model = pickle.load(open('models/heartDisease/model.pickle','rb'))
    return model.predict(df)[0]

def login():
    master = mongo.db.Users
    b = str(request.form.get("password_input", False))
    result = master.find_one({"Password":b})
    if result is not None:
        if b==result['Password']:
            return 1

    return 0        
    

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/departments", methods=['GET', 'POST'])
def departments():
    return render_template('departments.html')


    

   

@app.route("/kidney", methods=['GET', 'POST'])
def kidney():
    return render_template('kidney.html')

@app.route("/covid", methods=['GET', 'POST'])
def covid():
    return render_template('covid.htm')
    
@app.route("/dengue", methods=['GET', 'POST'])
def dengue():
    return render_template('dengue.html')

@app.route("/ParkinsonDisease", methods=['GET', 'POST'])
def ParkinsonDisease():
    return render_template('parkinsonDisease.html')

@app.route("/ThyroidDisease", methods=['GET', 'POST'])
def ThyroidDisease():
    return render_template('thyroidDisease.html')

@app.route("/malaria", methods=['GET', 'POST'])
def malaria():
    return render_template('malaria.html')

@app.route("/diabetes", methods=['GET', 'POST'])
def diabetes():
    return render_template('diabetes.html')
    
@app.route("/breastCancer", methods=['GET', 'POST'])
def breastCancer():
    return render_template('breastCancer.html')    

@app.route("/heartDisease", methods=['GET', 'POST'])
def heartDisease():
    return render_template('heartDisease.html')
    

@app.route("/login", methods=['GET', 'POST'])
def loginPage():
    return render_template('login.html')


@app.route("/userDashboard", methods=['GET', 'POST'])
def checkLogin():
    flag = login()
    if flag == 0:
        return render_template('login.html', text="Invalid Credential")
    else:
        return render_template('shady.html')    
       

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    master = mongo.db.Users
    a = str(request.form.get("name_input", False))
    b = str(request.form.get("password_input", False))
    post = {'Username': a, 'Password' : b}
    master.insert_one(post)
    
    return render_template('signup.html')    

 


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
    
    if pred == 1:
        res_val = "Patient is suffering from Kidney disease"
    else: 
        res_val = "Patient is not suffering from Kidney disease"
    master = mongo.db.predictKidney;  

    master.insert({'Test Report': res_val})
    return render_template('predictKidney.html', pred = pred)

@app.route("/predictCovid", methods = ['POST', 'GET'])
def predictCovid():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictKidney(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("index_content.html", message = message)
    
    if pred == 1:
        res_val = "Patient is suffering from Covid"
    else: 
        res_val = "Patient is not suffering from Covid"
    master = mongo.db.predictCovid;  

    master.insert({'Test Report': res_val})
    return render_template('predictCovid.html', pred = pred)

@app.route("/predictDiabetes", methods = ['POST', 'GET'])
def predictDiabetes():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictDiabetes(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("index_content.html", message = message)
    
    if pred == 1:
        res_val = "Patient is suffering from Diabetes"
    else: 
        res_val = "Patient is not suffering from Diabetes"
    master = mongo.db.predictDiabetes;  

    master.insert({'Test Report': res_val})
    return render_template('predictDiabetes.html', pred = pred)
    
@app.route("/predictDengue", methods = ['POST', 'GET'])
def predictDengue():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictDengue(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("index_content.html", message = message)
    
    if pred == 1:
        res_val = "Patient is suffering from Dengue"
    else: 
        res_val = "Patient is not suffering from Dengue"
    master = mongo.db.predictDiabetes;  

    master.insert({'Test Report': res_val})
    return render_template('predictDengue.html', pred = pred)
 
@app.route('/predictParkinsonDisease',methods=['POST', 'GET'])
def predictParkinson():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictParkinsonDisease(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("index_content.html", message = message)
    
    if pred == 1:
        res_val = "Patient is suffering from Parkinson Disease"
    else: 
        res_val = "Patient is not suffering from Parkinson Disease"
    master = mongo.db.predictDiabetes;  

    master.insert({'Test Report': res_val})
    return render_template('predictParkinson.html', pred = pred)

@app.route('/predictThyroidDisease',methods=['POST', 'GET'])
def predictThyroid():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = model_predictParkinsonDisease(to_predict_list)
    except:
        message = "Please enter valid Data"
        return render_template("index_content.html", message = message)
    
    if pred == 1:
        res_val = "Patient is suffering from Thyroid Disease"
    else: 
        res_val = "Patient is not suffering from Thyroid Disease"
    master = mongo.db.predictDiabetes;  

    master.insert({'Test Report': res_val})
    return render_template('predictThyroid.html', pred = pred)
    
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
    
@app.route('/predictBreastCancer',methods=['POST'])
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
          
    master = mongo.db.predictBreastCancer; 


    master.insert({'Test Report': res_val})
    return render_template('breastCancer.html', prediction_text='Patient has {}'.format(res_val))   



@app.route('/predictHeartDisease',methods=['POST'])
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
        
  
    master = mongo.db.predictHeartDisease; 


    master.insert_one({'Test Report': res_val})
    return render_template('heartDisease.html', prediction_text='Patient has {}'.format(res_val))    



     
    




if __name__ == '__main__':
	app.run(debug=True)
