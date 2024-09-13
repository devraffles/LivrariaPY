import streamlit as st
import pandas as pd
import plotly.express as px  

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("DB/customer reviews.csv")
df_top100_books = pd.read_csv("DB/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()
media_price = df_top100_books["book price"].mean()

filter_price = st.sidebar.slider("Price Range", price_min, price_max, media_price)

df_books = df_top100_books[df_top100_books["book price"] <= filter_price]

df_books

fig_year = px.bar(df_books["year of publication"].value_counts())
fig_price = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(fig_year)
col2.plotly_chart(fig_price)