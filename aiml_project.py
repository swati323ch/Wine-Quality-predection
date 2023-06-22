# -*- coding: utf-8 -*-
"""AIML Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hk861iMDp86IGtAghRFSHrKMVfyyj0lD
"""

import numpy as np
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

"""#Reading CSV file

"""

#loading the wine dataset
wine_data = pd.read_csv('/content/final 2 wine2.csv')

"""#Data set description

"""

wine_data.tail()

wine_data.head(20)

"""#Elimination of null values"""

#checking missing values
wine_data.isnull().sum()

msno.matrix(wine_data);

#dropping null values
wine_data=wine_data.dropna()
wine_data

wine_data.shape

wine_data.size

#DATA ANALYSIS AND VISUALISATION By statistical measurs
wine_data.describe()

"""Distribution of data on the basis of Quality"""

print(wine_data['quality'].unique())
print(wine_data['quality'].value_counts())

"""#Visualisation of Data"""

#number of values for each quality
sns.catplot(x='quality',data = wine_data, kind ='count')

#volatile acidity vs quality
plot = plt.figure(figsize=(4,4))
sns.barplot(x= 'quality' , y='volatile acidity',data = wine_data)

#volatile acidity vs quality
plot = plt.figure(figsize=(4,4))
sns.barplot(x= 'quality' , y='citric acid',data = wine_data)

plt2 = plt.figure(figsize = (4,4))
sns.barplot(x='quality' , y='alcohol',data=wine_data)

sns.pairplot(wine_data)

"""#Correlation"""

correlation = wine_data.corr()

# to construct heatmap
plt.figure(figsize = (7,7))
sns.heatmap(correlation, cbar=True, square=True,fmt = '.2f',annot=True,annot_kws={'size':8},cmap='coolwarm')

"""#Data Preprocessing"""

#data preprocessing
#seperate data and lable
Y = wine_data.drop('quality',axis =1)
Y

#X = wine_data['quality']

"""Lable Binerisation"""

#lable binerisation
Z = wine_data['quality'].apply(lambda z_value:1 if z_value>=7 else 0)

X = wine_data['quality'].apply(lambda y_value: y_value if y_value >=7 else y_value)

print(X)

"""#Spliting data into training and testing data"""

Y_train, Y_test, X_train, X_test =train_test_split(Y, Z,test_size=0.2,random_state=25)

print(Y.shape,Y_train.shape,Y_test.shape)

model = RandomForestClassifier()
model.fit(Y_train, X_train)

#accuracy on test data
Y_test_prediction = model.predict(Y_test)
test_data_accuracy =accuracy_score(Y_test_prediction,X_test)
print(test_data_accuracy)

"""#Model Training"""

Y_train, Y_test, X_train, X_test =train_test_split(Y, X,test_size=0.2,random_state=25)

df = RandomForestClassifier()
df.fit(Y_train, X_train)

#accuracy on test data
Y_test_prediction =df.predict(Y_test)
test_data_accuracy2 =accuracy_score(Y_test_prediction,X_test)
print(test_data_accuracy2)

#import joblib
#df.fit(Y_train, X_train)
#joblib.dump(model, 'wine_quality_model.joblib')

"""#User Input"""

user_input = (7.0	,0.27,	0.36,	20.70,	0.045,	45.0,	170.0,	1.0010,	3.00,0.45,8.8)
#user_input = (6.6,0.16,0.40,1.50,0.044,48.0,143.0,0.9912,3.54,0.52,12.4)

#changing the input data to numpy array
user_input_np = np.asarray(user_input)
user_input_reshape = user_input_np.reshape(1,-1)
predection = model.predict(user_input_reshape)
print(predection)
predection_in_binary_form = rf.predict(user_input_reshape)
print(predection_in_binary_form)
if (predection==1):
  print("good quality")
else:
 print("not good quality")
if (predection ==3):
  print("Below 10%")
elif(predection == 4):
  print("quality between 10% to 25%")
elif(predection == 5):
  print("quality between 25% to 40%")
elif(predection == 6):
  print("quality between 40% to median%")
elif(predection == 7):
  print("quality between median% to 75%")
elif(predection == 8):
  print("quality between 75% to 90%")
elif(predection == 9):
  print("quality above 90%")