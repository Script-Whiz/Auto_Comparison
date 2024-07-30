import streamlit as st
import pandas as pd
import plotly.express as px


# Load the data from the CSV file
autos = pd.read_csv('autos_data.csv')

# Create a header
st.header("Comparison of Auto Sales from 1908-2019")

