
#In[1]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
#In[2]
path="Covid-Dataset.csv"
df = pd.read_csv(path)
sample=pd.DataFrame(df)

#In[3]
print(df.dtypes)
print(df.head)
sample.Breathing_Problem.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Fever.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Dry_Cough.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Sore_throat.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Running_Nose.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Asthma.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Chronic_Lung_Disease.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Headache.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Heart_Disease.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Diabetes.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Hyper_Tension.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Fatigue.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Gastrointestinal.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Abroad_travel.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Contact_with_COVID_Patient.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Attended_Large_Gathering.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Visited_Public_Exposed_Places.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Family_working_in_Public_Exposed_Places.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Wearing_Masks.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.Sanitization_from_Market.replace(('Yes', 'No'), (1, 0), inplace=True)
sample.COVID.replace(('Yes', 'No'), (1, 0), inplace=True)


#In[4]
print(df.head())
print(df.dtypes)


#In[5]
X=df[['Breathing_Problem','Fever','Dry_Cough','Sore_throat','Running_Nose',
'Headache','Heart_Disease', 'Diabetes','Abroad_travel',
'Contact_with_COVID_Patient','Attended_Large_Gathering','Visited_Public_Exposed_Places',
'Family_working_in_Public_Exposed_Places','Wearing_Masks',
]]


#In[6]
X.head(30)



#In[7]
Y=df[['COVID']]


#In[8]
Y.head()


#In[9]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2,random_state=2)
x_train.shape, y_train.shape


#In[10]
from sklearn.ensemble import RandomForestClassifier
RF = RandomForestClassifier()
RF.fit(x_train, y_train)
y_pred = RF.predict(x_test)


#In[11]
import sklearn.metrics as skm
skm.multilabel_confusion_matrix(y_test, y_pred)
print(skm.classification_report(y_test, y_pred))


#In[12]
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print(accuracy)


#[13]
pickle.dump(RF, open('model.pkl','wb'))



#[14]
model=pickle.load(open('model.pkl','rb'))