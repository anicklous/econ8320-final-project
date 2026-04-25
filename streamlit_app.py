import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title(":green[ECON 8320] Final Project")
st.write("Updated monthly with the latest data from the Bureau of Labor Statistics")
st.divider()
st.write("Current Metrics and Month-to-Month Changes")
unoLogo = "https://www.unomaha.edu/office-of-strategic-marketing-and-communications/_files/uno-o-icon-color.png"
st.logo(unoLogo,
    link="https://www.unomaha.edu/office-of-strategic-marketing-and-communications/_files/uno-o-icon-color.png",
    icon_image=unoLogo)

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

e, f, g= st.columns(3)
h, i = st.columns(2)

hourlyMain = pd.DataFrame(avgHourly.head(2))
exportMain = pd.DataFrame(exportIndex.head(2))
importMain = pd.DataFrame(importIndex.head(2))
nonfarmMain = pd.DataFrame(nonfarm.head(2))
unempMain = pd.DataFrame(unempRate.head(2))

e.metric("Total Nonfarm Employment",nonfarmMain['value'][0], nonfarmMain['value'][0]-nonfarmMain['value'][1],border=True)
f.metric("Average Hourly Earnings",hourlyMain['value'][0], hourlyMain['value'][0]-hourlyMain['value'][1],border=True)
g.metric("Unemployment Rate", unempMain['value'][0], unempMain['value'][0]-unempMain['value'][1],border=True)

h.metric("Import Price Index", importMain['value'][0], importMain['value'][0]-importMain['value'][1],border=True)
i.metric("Export Price Index", exportMain['value'][0], exportMain['value'][0]-exportMain['value'][1],border=True)

st.sidebar.write("Click to learn more:")

if st.sidebar.button("Unemployment Rate"):
    st.markdown(
        """
        *Unemployment Rate*

        Unemployment rate is one of many indicators of an economy's health.

        To calculate it, divide the number of unemployed individuals by the total labor force, then multiply the ratio by 100.
        """)
    st.divider()
    st.caption("**Due to a lapse caused by the government shutdown, no data exists for October 2025*")
    st.caption("**Zoom in for more precision*")
    
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

        Total Nonfarm Employment counts the number of US workers in the economy, excluding proprietors, private household employees, unpaid volunteers, farm employees, and the unincorporated self-employed.

        According to the Federal Reserve Bank, nonfarm workers account for approximately 80% of the workers who contribute to Gross Domestic Product.
        """)
    st.divider()
    st.caption("**In thousands of employees*")

    monthChange = pd.DataFrame(nonfarm.head(2))
    yearChanges = pd.DataFrame(nonfarm[nonfarm['periodName']==nonfarm['periodName'][0]])

    a, b = st.columns(2)
    c, d = st.columns(2)

    a.metric("Current Total Nonfarm Employment",monthChange['value'][0], border=True)
    b.metric("Last Month",monthChange['value'][1], monthChange['value'][0]-monthChange['value'][1], border=True)

    c.metric("Last Year", yearChanges['value'][12], yearChanges['value'][0]- yearChanges['value'][12], border=True)
    d.metric("Two Years Ago", yearChanges['value'][24], yearChanges['value'][0]- yearChanges['value'][24], border=True)

if st.sidebar.button("Average Hourly Earnings"):
    st.markdown(
        """
        *Average Hourly Earnings*

        Average Hourly Earnings is a measure of the average hourly earnings of all private employees on a “gross” basis, including overtime pay.

        Average hourly earnings measure the actual return to a worker for a set period of time, rather than the amount contracted for a unit of work (the wage rate).
        """)
    st.divider()
    st.caption("**Private sector, seasonally adjusted*")
    
    st.write('**Average Hourly Earnings Spread by Year(USD)**')
    wageBox = px.box(avgHourly,y='value',color='year',labels={'value': 'Average Hourly Earnings (USD)',
                                                              'year': 'Year'})
    st.plotly_chart(wageBox)
    
if st.sidebar.button("Import Price Index"):
    st.markdown(
        """
        *Import Price Index*

        The Import Price Index measures the average change over time in the prices paid for non-military goods and services purchased from foreign suppliers and imported into the US.

        """)
    st.divider()
    st.caption("**Base period: 2000 = 100*")

    importTable = pd.DataFrame(importIndex)
    importTable = importTable[['year','periodName','value']]
    importTable.rename(columns={'year': 'Year', 'periodName': 'Month', 'value': 'Index'}, inplace=True)
    st.write(importTable)

if st.sidebar.button("Export Price Index"):
    st.markdown(
        """
        *Export Price Index*

        The Export Price Index measures the average change over time in the prices of goods and services produced domestically and sold to other countries.

        """)
    st.divider()
    st.caption("**Base period: 2000 = 100*")
    
    exportTable = pd.DataFrame(exportIndex)
    exportTable = exportTable[['year','periodName','value']]
    exportTable.rename(columns={'year': 'Year', 'periodName': 'Month', 'value': 'Index'}, inplace=True)
    st.write(exportTable)

st.sidebar.button("**Back to main**", type='tertiary')
st.sidebar.divider()
st.sidebar.page_link("https://www.bls.gov/developers/api_signature_v2.htm",label=":green[BLS API format]")
st.sidebar.page_link("https://data.bls.gov/toppicks?survey=bls",label=":green[Original data source]")
st.sidebar.divider()
st.sidebar.caption("Last updated: April 2026")