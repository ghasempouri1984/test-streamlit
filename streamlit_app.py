# Import Streamlit
#import streamlit as st

# Use Streamlit's magic commands to write "Hello, World!"
#st.write("Hello, World!")

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
country_df = pd.read_csv('countries.csv')

# First Viz
def viz1():
    total_erih_plus = 11128
    total_oc_meta = 8689
    coverage_percentage = (total_oc_meta / total_erih_plus) * 100
    remaining = 100 - coverage_percentage
    coverage_data = [coverage_percentage, remaining]
    labels = ['Covered in OpenCitations Meta', 'Not in OpenCitations Meta']
    plt.title('ERIH Plus Journals in OC Meta Coverage')
    sns.set_style("whitegrid")
    plt.pie(coverage_data, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    st.pyplot(plt)

# Second Viz
def viz2():
    meta_coverage_df = pd.read_csv('<your file>')  # replace '<your file>' with your actual file path
    access_counts = meta_coverage_df['Open Access'].value_counts()
    plt.figure(figsize=(6, 6))
    sns.set_style("whitegrid")
    plt.pie(access_counts, labels=access_counts.index, autopct='%1.1f%%')
    plt.title('Open Access Status')
    st.pyplot(plt)

# Third Viz
def viz3():
    color_scale = [
        [0.0, '#f7fbff'],
        [0.001, '#deebf7'],
        [0.002, '#c6dbef'],
        [0.005, '#9ecae1'],
        [0.10, '#6baed6'],
        [0.20, '#4292c6'],
        [0.30, '#2171b5'],
        [0.40, '#08519c'],
        [0.50, '#08306b'],
        [1.0, '#081d58'],
    ]
    fig = px.choropleth(country_df, locations='Country',
                        locationmode='country names',
                        color='Publication_count',
                        hover_name='Country',
                        color_continuous_scale=color_scale,
                        title='Publications by Country')
    st.plotly_chart(fig)

# Streamlit code
def main():
    st.title("Visualizations")
    st.header("ERIH Plus Journals in OC Meta Coverage")
    viz1()
    st.header("Open Access Status")
    viz2()
    st.header("Publications by Country")
    viz3()

if __name__ == "__main__":
    main()

