import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("DB/customer reviews.csv")
df_top100_books = pd.read_csv("DB/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
serch_book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["book title"] == serch_book]
df_reviews_f = df_reviews[df_reviews["book name"] == serch_book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)

col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

st.divider()

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])