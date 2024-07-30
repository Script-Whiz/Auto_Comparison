import streamlit as st
import pandas as pd
import plotly.express as px


# Load the data from the CSV file
autos = pd.read_csv('autos_data.csv')

# Create a header
st.header("Comparison of Auto Sales from 1908-2019")

# Add a checkbox
show_only_automatic = st.checkbox("Show Only Automatic Transmissions")

# Create a filtered DataFrame based on the checkbox
if 'transmission' in autos.columns:
    if show_only_automatic:
        filtered_autos = autos[autos['transmission'] == 'automatic']
    else:
        filtered_autos = autos
    # Get counts of each transmission type from the filtered dataset
    transmission_counts = filtered_autos['transmission'].value_counts().reset_index()
    transmission_counts.columns = ['transmission', 'count']
    
    # Ensure transmission counts are not empty
    if not transmission_counts.empty:
        # Create a histogram using Plotly
        fig = px.bar(transmission_counts, x='transmission', y='count', title='Counts of Each Transmission Type')
        
        # Display histogram in Streamlit
        st.write("Here is a histogram of the counts of each transmission type:")
        st.plotly_chart(fig)
    else:
        st.write("No data available for the selected transmission types.")
else:
    st.error("The 'transmission' column is missing from the data.")
    
