#import packages
import streamlit as st
import pandas as pd
import numpy as np


st.title('Stars: Temperature (K), Luminosity(L/Lo), Radius(R/Ro), Spectral Class, Color, and Absolute Magnitude')


# load in data
df = pd.read_csv('https://raw.githubusercontent.com/zf81/dashboard-streamlit/main/data/Stars.csv')
df = df.head(100)


## Header ##
st.header('Star Features')
st.subheader('Spectral Class, Color, Luminosity, Absolute Magnitude')
## Caption ##
st.caption('This dataset includes the various features of stars that are utilizied in the  Hertzsprung-Russell diagram (HR diagram), which is one of the most important tools in the study of stellar evolution.')

## Toggle ##
if st.checkbox('Show first 1000 records of Stars dataset'):
    st.dataframe(df)

## Code Block  ##
code= '''def scroll(): print("Scroll Down To See Charts")'''
st.code(code, language='python')

## Dataframe and Chart 1: Star Temperature and Luminosity  ##
st.subheader('Temperature of Stars Against Their Luminosity ')

stars = pd.read_csv('https://raw.githubusercontent.com/zf81/dashboard-streamlit/main/data/Stars.csv')

temperature = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["temperature", "luminosity"])

st.bar_chart(temperature)



################################################################
## Dataframe and Chart 1: BMI Levels ##
st.subheader('BMI Levels Among Patients')

diabetes = pd.read_csv('diabetes.csv')

BMI = diabetes['BMI'].value_counts()

st.bar_chart(BMI)

st.caption("This bar chart illustrates the count of unique BMI levels among female patients.")

## DataFrame and Chart 2: Vitals Among Patients ##
st.subheader('Vitals Levels Among Patients')

chart_data = pd.DataFrame(np.random.randn(20, 4), columns=['Glucose','Insulin','BloodPressure', 'Pregnancies'])

st.line_chart(chart_data)

st.caption("This line chart illustrates to vitals levels of female patients used as diagnostic measurements to predict diabetes.")
 























