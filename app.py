import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Load and clean data
data = pd.read_csv("vehicles_us.csv")
data['is_4wd'] = data['is_4wd'].fillna(0).astype(int)
data['date_posted'] = pd.to_datetime(data['date_posted'], format='%Y-%m-%d')
data['model_year'] = data['model_year'].fillna("not specified")
data['paint_color'] = data['paint_color'].fillna("not specified")
data['odometer'] = data['odometer'].fillna(np.nan)
data['cylinders'] = data['cylinders'].fillna("not specified")

# Ensure all values in model_year are strings for consistency
data["model_year"] = pd.to_numeric(data["model_year"], errors="coerce")  # Convert to numeric, set invalid to NaN
model_years = sorted(data["model_year"].dropna().unique())  # Drop NaNs and sort

# Streamlit headers and data viewer
st.header("Vehicles Data Viewer")
st.dataframe(data)

# Histogram: Most Valuable Vehicle Type
st.header("Most Valuable Vehicle Type")
price_vs_vehicle_type_hist = px.histogram(
    data,
    x="type",
    y="price",
    title="Most Valuable Vehicle Type",
    labels={"type": "Vehicle Type", "price": "Vehicle Price ($)"},
    histfunc='avg',
    color="type"
)
st.plotly_chart(price_vs_vehicle_type_hist)

# Scatter Plot: Odometer and Price Correlation
st.header("Odometer and Price Correlation")
filtered_data = data[data['odometer'].notna()]
odometer_vs_price_scatter = px.scatter(
    filtered_data,
    x="odometer",
    y="price",
    title="Odometer and Price Correlation",
    labels={"odometer": "Odometer (Mileage)", "price": "Vehicle Price ($)"},
    opacity=0.6
)
st.plotly_chart(odometer_vs_price_scatter)

# Compare Price Distribution Between Model Years
st.header("Compare Price Distribution Between Model Years")

# Dropdowns for selecting years
year_1 = st.selectbox("Select Year 1", model_years, index=0)
year_2 = st.selectbox("Select Year 2", model_years, index=1)

# Filter data for the selected years
selected_years = data[data["model_year"].isin([year_1, year_2])]

# Checkbox to normalize histogram
normalize = st.checkbox("Normalize histogram", value=True)
histnorm = "percent" if normalize else None

# Create a histogram to compare price distribution between selected model years
price_comparison_hist = px.histogram(
    selected_years,
    x="price",
    color="model_year",
    nbins=30,
    histnorm=histnorm,
    barmode="overlay",
    title="Price Distribution Comparison Between Model Years",
    labels={"price": "Vehicle Price ($)", "model_year": "Model Year"}
)
st.plotly_chart(price_comparison_hist)

# Bar Plot: Paint Color Availability
st.header("Paint Color Distribution")
paint_color_bar = px.bar(
    data.groupby('paint_color')['price'].count().reset_index().rename(columns={'price': 'Count'}),
    x="paint_color",
    y="Count",
    title="Paint Color Distribution",
    labels={"paint_color": "Paint Color", "Count": "Number of Vehicles"},
    color="paint_color"
)
st.plotly_chart(paint_color_bar)

