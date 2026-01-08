import streamlit as st
import numpy as np
import joblib

model = joblib.load('svm_model.pkl')

st.title('Survival perdiction')
st.write('Enter the passenger details')

pclass=st.selectbox('Passenger Class',[1,2,3])
Age=st.number_input('Enter the Age',0,100)
Fare=st.number_input('Enter the fare price',0,600)
sex=st.selectbox('Choose the gender',['male','female'])
Embarked=st.selectbox('Choose the Embarked',['S','C','Q'])
Family_size=st.number_input('Enter the the Family size if u Alone enter 1',min_value=1,max_value=20)

sex_numeric= 1 if sex == 'male' else 0

Embarked_C = 0
Embarked_Q = 0
Embarked_S = 0

if Embarked == 'S':
    Embarked_S=1
elif Embarked== 'C':
    Embarked_C=1
elif Embarked== "Q":
    Embarked_Q=1

X_input=np.array([pclass,Age,Fare,sex,Embarked_S,Embarked_C,Embarked_Q,Family_size])

if st.button['Predict']:
    pred=model.predict(X_input)
    if pred[0] == 1:
        st.success("The model predicts: Survived ✅")
    else:
        st.error("The model predicts: Died ❌")