import streamlit as st
import pandas as pd
import numpy as np

st.title(":green[ECON 8320] Final Project")
st.write("A display including most recent data from the Bureau of Labor Statistics")

avgHourly = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/avgHourly.csv")
exportIndex = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/exportIndex.csv")
importIndex = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/importIndex.csv")
nonfarm = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/nonfarm.csv")
unempRate = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/unempRate.csv")

avgHourly['year'] = avgHourly['year'].astype(str)
exportIndex['year'] = exportIndex['year'].astype(str)
importIndex['year'] = importIndex['year'].astype(str)
nonfarm['year'] = nonfarm['year'].astype(str)
unempRate['year'] = unempRate['year'].astype(str)

order = ['January','February','March',
         'April','May','June',
         'July','August','September',
         'October','November','December']

avgHourly['periodName'] = pd.Categorical(avgHourly['periodName'], categories=order, ordered=True)
exportIndex['periodName'] = pd.Categorical(exportIndex['periodName'], categories=order, ordered=True)
importIndex['periodName'] = pd.Categorical(importIndex['periodName'], categories=order, ordered=True)
nonfarm['periodName'] = pd.Categorical(nonfarm['periodName'], categories=order, ordered=True)
unempRate['periodName'] = pd.Categorical(unempRate['periodName'], categories=order, ordered=True)

st.sidebar.write("What would you like to see?")
if st.sidebar.button("Unemployment Rates"):
    st.write('**Unemployment Rate Over Time**')
    st.line_chart(unempRate,x= 'periodName',                  
                  y='value',
                  x_label='Month',
                  y_label='Unemployment Rate (%)',
                  color='year',
                  width=800)        
st.sidebar.button("Total Nonfarm Employment")
if st.sidebar.button("Average Hourly Wages"):
    st.write('**Average Hourly Wage (USD) by Month**')
    st.line_chart(avgHourly,x= 'periodName',
                  y='value',
                  x_label='month',
                  y_label='Average Hourly Wage (USD)',
                  color='year',
                  width=400)
st.sidebar.button("Import Price Index")
st.sidebar.button("Export Price Index")
st.sidebar.write("Please choose a time period:")
st.sidebar.selectbox("Year",["2026","2025","2024"])
st.sidebar.page_link("https://www.bls.gov/developers/api_signature_v2.htm",label=":green[BLS API format]")
st.sidebar.page_link("https://data.bls.gov/toppicks?survey=bls",label=":green[Original data source]")
st.sidebar.caption("Last updated: April 2026")

