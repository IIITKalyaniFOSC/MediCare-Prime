from flask import Flask, render_template, Response, jsonify, request

from modules.cardio import heartDisease
from modules.patho import kidney, malaria, diabetes, dengue
from modules.onco import breastCancer
from modules.ent import covid

app = Flask(__name__)

app.register_blueprint(heartDisease.heart_disease)
app.register_blueprint(kidney.kidney)
app.register_blueprint(malaria.malaria)
app.register_blueprint(dengue.dengue)
app.register_blueprint(diabetes.diabetes)
app.register_blueprint(breastCancer.breast_cancer)
app.register_blueprint(covid.covid)

#app.register_blueprint(auth)

    
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/departments", methods=['GET', 'POST'])
def departments():
    return render_template('departments.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')   

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template('signup.html') 

if __name__ == '__main__':
	app.run(debug="true")