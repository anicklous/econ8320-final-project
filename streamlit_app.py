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
st.sidebar.page_link("https://www.bls.gov/developers/api_signature_v2.htm",label=":blue[BLS API format]")
st.sidebar.page_link("https://data.bls.gov/toppicks?survey=bls",label=":blue[Original data source]")

st.title("📈ECON 8320 Final Project📉")
st.write("Updated monthly with published data from the Bureau of Labor Statistics")