import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title(":blue[ECON 8320] Final Project")
st.write("A display including most recent data from the Bureau of Labor Statistics")
st.divider()

#I wanted to configure a color theme with a TOML file, but I couldn't figure out how
avgHourly = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/avgHourly.csv")
exportIndex = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/exportIndex.csv")
importIndex = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/importIndex.csv")
nonfarm = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/nonfarm.csv")
unempRate = pd.read_csv("https://raw.githubusercontent.com/anicklous/econ8320-final-project/refs/heads/main/unempRate.csv")

avgHourly['value'] = avgHourly['value'].replace("-",None)
exportIndex['value'] = exportIndex['value'].replace("-",None)
importIndex['value'] = importIndex['value'].replace("-",None)
nonfarm['value'] = nonfarm['value'].replace("-",None)
unempRate['value'] = unempRate['value'].replace("-",None)


avgHourly['year'] = avgHourly['year'].astype(str)
exportIndex['year'] = exportIndex['year'].astype(str)
importIndex['year'] = importIndex['year'].astype(str)
nonfarm['year'] = nonfarm['year'].astype(str)
unempRate['year'] = unempRate['year'].astype(str)

avgHourly['value'] = avgHourly['value'].astype(float)
exportIndex['value'] = exportIndex['value'].astype(float)
importIndex['value'] = importIndex['value'].astype(float)
nonfarm['value'] = nonfarm['value'].astype(int)
unempRate['value'] = unempRate['value'].astype(float) 

order = ['January','February','March',
         'April','May','June',
         'July','August','September',
         'October','November','December']

avgHourly['periodName'] = pd.Categorical(avgHourly['periodName'], categories=order, ordered=True)
exportIndex['periodName'] = pd.Categorical(exportIndex['periodName'], categories=order, ordered=True)
importIndex['periodName'] = pd.Categorical(importIndex['periodName'], categories=order, ordered=True)
nonfarm['periodName'] = pd.Categorical(nonfarm['periodName'], categories=order, ordered=True)
unempRate['periodName'] = pd.Categorical(unempRate['periodName'], categories=order, ordered=True)

st.sidebar.write("Click to learn more:")

if st.sidebar.button("Unemployment Rate"):
    st.markdown(
        """
        *Unemployment Rate*

        Unemployment rate is one of many indicators of an economy's health.

        To calculate it, divide the number of unemployed individuals by the total labor force, then multiply the ratio by 100.
        """)
    st.caption("**Due to a lapse caused by the government shutdown, no data exists for October 2025*")
    st.caption("**Zoom in for more precision*")
    st.divider()

    st.write('**Unemployment Rates by Month and Year**')
    st.line_chart(unempRate,x= 'periodName',                  
                  y='value',
                  x_label='Month',
                  y_label='Unemployment Rate (%)',
                  color='year',
                  width=800)    
        
if st.sidebar.button("Total Nonfarm Employment"):
    st.markdown(
        """
        *Total Nonfarm Employment*

        Total nonfarm employment counts the number of US workers in the economy, excluding proprietors, private household employees, unpaid volunteers, farm employees, and the unincorporated self-employed.

        According to the Federal Reserve Bank, nonfarm workers account for approximately 80 percent of the workers who contribute to Gross Domestic Product.
        """)
    st.divider()

if st.sidebar.button("Average Hourly Wages"):
    st.markdown(
        """
        *Average Hourly Wages*

        Unemployment rate is one of many indicators of an economy's health.

        To calculate it, divide the number of unemployed individuals by the total labor force, then multiply the ratio by 100.
        """)
    st.caption("**Private sector, seasonally adjusted*")
    st.divider()

    st.write('**Ranges by Year: Average Hourly Wage (USD)**')
    wageBox = px.box(avgHourly,y='value',color='year')
    st.plotly_chart(wageBox)
    
if st.sidebar.button("Import Price Index"):
    st.markdown(
        """
        *Import Price Index*

        The Import Price Index (IPI) measures the average change over time in the prices paid for non-military goods and services purchased from foreign suppliers and imported into the US.

        """)
    st.caption("**Base period: 2000 = 100*")
    st.divider()

    st.dataframe(importIndex,hide_index=True,column_order=('year','periodName','value'))

if st.sidebar.button("Export Price Index"):
    st.markdown(
        """
        *Export Price Index*

        The Export Price Index (XPI) measures the average change over time in the prices of goods and services produced domestically and sold to other countries.

        """)
    st.caption("**Base period: 2000 = 100*")
    st.divider()

    st.dataframe(exportIndex,hide_index=True,column_order=('year','periodName','value'))

st.sidebar.button("**Back to main**", type='tertiary')
st.sidebar.divider()
st.sidebar.page_link("https://www.bls.gov/developers/api_signature_v2.htm",label=":blue[BLS API format]")
st.sidebar.page_link("https://data.bls.gov/toppicks?survey=bls",label=":blue[Original data source]")
st.sidebar.divider()
st.sidebar.caption("Last updated: April 2026")

st.dataframe(nonfarm,hide_index=True,column_order=('year','periodName','value'))
