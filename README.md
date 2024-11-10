# Car Sales Analysis Web Application

This project is a Streamlit web application that analyzes car sales data, providing insights into price distributions, odometer readings, and conditions. Users can interactively explore data with histograms, scatter plots, and more.

### Live Demo
[View the application on Render](https://car-sales-web-app-fycl.onrender.com)

### Project Structure
- `app.py`: The main Streamlit app file.
- `cleaned_vehicles_us.csv`: The dataset used in the application.
- `notebooks/EDA.ipynb`: Exploratory Data Analysis notebook.
- `.streamlit/config.toml`: Streamlit configuration for deployment on Render.

## Features
- **View Raw Data**: Toggle to show the raw car sales data.
- **Price Distribution**: Histogram showing the distribution of car prices.
- **Price vs. Model Year**: Scatter plot of price vs. model year, colored by condition.

### Getting Started
To run the application locally, clone the repository, install requirements, and run:

```bash
streamlit run app.py

