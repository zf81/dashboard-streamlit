#import packages
import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv('https://raw.githubusercontent.com/zf81/dashboard-streamlit/main/data/Stars.csv')

# Fix column names 
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
df.columns = df.columns.str.lower()
df.columns.values

#### Put together dataframes ####
df_temp = df.filter(['Temperature (K)','Luminosity(L/Lo)','Radius(R/Ro)'])
# Get rid of irrelevant rows
df_temp = df_temp[df_temp['Luminosity(L/Lo)'].apply(lambda x: str(x).isdigit())]
df_temp = df_temp[df_temp['Radius(R/Ro)'].apply(lambda x: str(x).isdigit())]
df_temp = df_temp[df_temp['Temperature (K)'].str.contains('Unknown')==False ]
# Convert columns to integers
df_temp['Luminosity(L/Lo)'] = df_temp['Luminosity(L/Lo)'].astype(int)
df_temp['Radius(R/Ro)'] = df_temp['Radius(R/Ro)'].astype(int)
# Group by temperature and get sum of each group
df_temp = df_temp.groupby('Temperature (K)').sum()


df_class = df.filter(['Spectral Class','Star color','Absolute magnitude(Mv)'])
# Get rid of irrelevant rows
df_class = df_class[df_class['Star color'].apply(lambda x: str(x).isdigit())]
df_class = df_class[df_class['Absolute magnitude(Mv)'].apply(lambda x: str(x).isdigit())]
# Convert columns to integers
df_class['Star color'] = df_class['Star color'].astype(int)
df_class['Absolute magnitude(Mv)'] = df_class['Absolute magnitude(Mv)'].astype(int)
# Group by Spectral Class and get sum of each group
df_class = df_class.groupby('Spectral Class').sum()

#### Putting together streamlit dashboard ####
st.title('Stars: Temperature (K), Luminosity(L/Lo), Radius(R/Ro), Spectral Class, Color, and Absolute Magnitude')

st.subheader('Stars: Temperature (K), Luminosity(L/Lo), Radius(R/Ro)')
st.text('This dataframe and chart displays the temperature, luminosity, and radii of different stars')
st.dataframe(df_temp)
st.bar_chart(df_temp)

st.subheader('Stars: Spectral Class, Color, and Absolute Magnitude')
st.text('This dataframe and chart displays the spectral class, color, and absolute magnitude of different stars')
st.dataframe(df_class)
st.line_chart(df_class)
