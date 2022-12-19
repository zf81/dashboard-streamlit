#import packages
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

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
st.subheader('Temperature (K) of Stars Against Their Luminosity (L/lo) ')

stars = pd.read_csv('https://raw.githubusercontent.com/zf81/dashboard-streamlit/main/data/Stars.csv')

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['temperature', 'luminosity'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='temperature', y='luminosity', tooltip=['temperature', 'luminosity'])

st.altair_chart(c, use_container_width=True)

st.caption("This alt air chart displays the temperatures of different stars in Kelvin against their luminosities (L/lo).")


## DataFrame and Chart 2: Spectral Classes and Colors of Stars ##

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['spectral class', 'color'])

st.line_chart(chart_data)

st.caption("This line chart displays the diffrent spectral classes and colors of stars.")

st.code(code, language='python')






















