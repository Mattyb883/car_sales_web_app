import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned dataset
df = pd.read_csv("cleaned_vehicles_us.csv")

# Title and description
st.title("Car Sales Dashboard")
st.header("Explore Used Car Prices and Conditions")

# Checkbox to toggle data view
if st.checkbox("Show raw data"):
    st.write(df)

# Plot 1: Histogram for car prices
st.subheader("Distribution of Car Prices")
fig_price = px.histogram(df, x="price", title="Distribution of Car Prices")
st.plotly_chart(fig_price)

# Plot 2: Scatter plot for price vs. model year with condition as color
st.subheader("Price vs. Model Year")
fig_scatter = px.scatter(
    df, x="model_year", y="price", color="condition",
    size="odometer", title="Price vs. Model Year (Bubble Size: Odometer Reading)",
    labels={'model_year': 'Model Year', 'price': 'Car Price (USD)'}
)
st.plotly_chart(fig_scatter)
