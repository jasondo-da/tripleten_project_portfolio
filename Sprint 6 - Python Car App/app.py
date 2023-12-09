# importing all the libraries we are going to use for this project
import streamlit as st
import pandas as pd
import plotly_express as px

# loading the raw data file
df = pd.read_csv('vehicles_us.csv')

# cleaning the data (getting rid of columns that we are not going to use for this project)
unused_columns = ['cylinders',
                  'fuel',
                  'transmission',
                  'paint_color',
                  'is_4wd',
                  'date_posted']
df = df.drop(unused_columns, axis='columns')

# creating a new column by spltting the the 'model' column results
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# text header of raw data display
st.header('Data Viewer')
# displaying the raw data with streamlit
st.dataframe(df)

# text header for "vehicle type manufacturer"
st.header('Vehicle Types by Manufacturer')
# creating histogram graphic for "vehicle type manufacturer"
fig = px.histogram(df, x='manufacturer', 
                   color='type')
# display the histogram with streamlit
st.write(fig)

# text header for "vehicle condition to the model year"
st.header('Histogram of `condition` vs `model_year`')
# creating histogram graphic for vehicle condition to the model year"
fig = px.histogram(df, x='model_year', 
                   color='condition')
# display the histogram with streamlit
st.write(fig)

# text header for "vehicle price to odometer"
st.header('Scatter Plot of `price` vs `odometer`')
# creating scatter plot graphic for "vehicle price to odometer"
fig = px.scatter(df, x='odometer', 
                   y='price')
# display the scatter plot with streamlit
st.write(fig)

# text header for "vehicle days listed to price"
st.header('Scatter Plot of `days_listed` vs `price`')
# creating scatter plot graphic for "vehicle days listed to price"
fig = px.scatter(df, x='days_listed', 
                   y='price')
# display the scatter plot with streamlit
st.write(fig)

# text header for "vehicle odometer to days listed"
st.header('Scatter Plot of `odometer` vs `days_listed`')
# creating scatter plot graphic for "vehicle odometer to days listed"
fig = px.scatter(df, x='days_listed', 
                   y='odometer')
# display the scatter plot with streamlit
st.write(fig)

# text header for "compare price distribution between manufacturers"
st.header('Compare Price Distribution Between Manufacturers')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# get user's inputs from a dropdown menu
manufacturer_1 = st.selectbox(
                              label='Select manufacturer 1', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )
# repeat for the second dropdown menu
manufacturer_2 = st.selectbox(
                              label='Select manufacturer 2',
                              options=manufac_list, 
                              index=manufac_list.index('hyundai')
                              )
# filter the dataframe 
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# create a plotly histogram figure
fig = px.histogram(df_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')
# display the figure with streamlit
st.write(fig)