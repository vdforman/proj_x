import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('vehicles_us.csv')

st.header("Project 4", anchor="Vehicles", divider='red')

import matplotlib as plt
#fdf = pd.read_csv('vehicles_us.csv')
df['is_4wd'] = df['is_4wd'].fillna(0)
df['is_4wd'] = df['is_4wd'].astype('int')
df['date_posted'] = pd.to_datetime(df['date_posted'] ,format='%Y-%m-%d')
df['model_year'] = df['model_year'].fillna("not specified")
df['paint_color'] = df['paint_color'].fillna("not specified")
df['odometer'] = df['odometer'].fillna("not specified")
df['cylinders'] = df['cylinders'].fillna("not specified")
df_suv = df[df['type'] == 'SUV']
df_pickup = df[df['type'] == 'pickup']
df_sedan = df[df['type'] == 'sedan']
df_truck = df[df['type'] == 'truck']
df_coupe = df[df['type'] == 'coupe']
df_van = df[df['type'] == 'van']
df_convertible = df[df['type'] == 'convertible']
df_hatchback = df[df['type'] == 'hatchback']
df_wagon = df[df['type'] == 'wagon']
df_minivan = df[df['type'] == 'mini_van']
df_offroad = df[df['type'] == 'offroad']
df_bus = df[df['type'] == 'bus']
df_type_other = df[df['type'] == 'other']

suv = st.checkbox("SUV", value=True)
pickup = st.checkbox("Pickup")
sedan = st.checkbox("Sedan")
truck = st.checkbox("Truck")
coupe = st.checkbox("Coupe")
van = st.checkbox("Van")
convertible = st.checkbox("Convertible")
hatchback = st.checkbox("Hatchback")
wagon = st.checkbox("Wagon")
minivan = st.checkbox("Minivan")
offroad = st.checkbox("Offroad")
bus = st.checkbox("Bus")
other = st.checkbox("Other")

if suv :
    print(df_suv['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price'))

if pickup :
    print(df_pickup['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if sedan :
    print(df_sedan['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if truck :
    print(df_truck['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if coupe :
    print(df_coupe['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if van :
    print(df_van['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if convertible :
    print(df_convertible['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if hatchback :
    print(df_hatchback['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if wagon :
    print(df_wagon['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if minivan :
    print(df_minivan['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if offroad :
    print(df_offroad['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if bus :
    print(df_bus['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

if other :
    print(df_type_other['price'].plot(kind='hist', bins=30, title='Type of Vehicle Price Availability', xlabel='Price', alpha=0.8))

color_bar = df.groupby('paint_color')['price'].count().plot(kind='bar', title='Color Availability', x='paint_color', ylabel= "Count")
type_bar = df.groupby("type")['price'].count().plot(kind='bar', title='Vehicle Type Availability', x='type', ylabel='Count', color='red')
df_proper_odo = df[df['odometer'] != 'not specified']
odo_price_scat = df_proper_odo.loc[:,['odometer','price']].plot(kind='scatter', title='Odometer vs Price', x='odometer', xlabel='Miles', y='price', alpha=0.5)


scat = px.scatter(df_proper_odo, x='odometer', y='price')
st.plotly_chart(scat)

