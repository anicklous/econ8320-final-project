import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.write("What would you like to see?")
st.sidebar.button("Unemployment Rates")
st.sidebar.button("Total Nonfarm Employment")
st.sidebar.button("Average Hourly Wages")
st.sidebar.button("Import Price Index")
st.sidebar.button("Export Price Index")
st.sidebar.write("Please choose a time period:")
st.sidebar.selectbox("Year",["2024","2025","2026"])

st.title("📈ECON 8320 Final Project📉")
st.markdown(
    """ 
    Updated monthly with public data from the Bureau of Labor Statistics  
    """)

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "$12K", "8%")
col2.metric("Users", "1,204", "12%")
col3.metric("Latency", "42ms", "-3%")

tab1, tab2, tab3 = st.tabs(["Chart", "Data", "Settings"])

with tab1:
    st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
with tab2:
    st.dataframe({"col1": [1, 2, 3], "col2": [4, 5, 6]})
with tab3:
    st.checkbox("Show gridlines")