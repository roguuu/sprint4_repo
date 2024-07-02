import pandas as pd
import streamlit as st
import plotly_express as px
#import os 

#print(os.getcwd())

df = pd.read_csv('sprint4_repo/cleaned_vehicles_us.csv')

st.header('Vehicles Dashboard')

fig_hist = px.histogram(df, x='price', nbins=30, 
                   title='Distribution of Vehicle Prices',
                   labels={'price': 'Price (USD)'},
                   template='plotly_white')

st.plotly_chart(fig_hist)


fig_scatter = px.scatter(df, x='odometer', y='price', 
                 title='Price vs. Odometer Reading',
                 labels={'odometer': 'Odometer (miles)', 'price': 'Price (USD)'},
                 template='plotly_white')

st.plotly_chart(fig_scatter)


if st.checkbox('Average Price Line on Scatter Plot'):
    avg_price = df['price'].mean()
    fig_scatter.add_hline(y=avg_price, line_dash='dash', line_color='red',
                          annotation_text=f'Average Price: ${avg_price:.2f}')
    st.plotly_chart(fig_scatter)

    