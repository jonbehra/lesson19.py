import streamlit as st
import pandas as pd
import plotly.express as px


# Load the dataset
books_df = pd.read_csv('file.csv')


# Streamlit app title and description
st.title("Bestselling Books Analysis")
st.write("This app analyzes the Amazon Top Selling books from 2009 to 2022.")


# Summary Statistics
st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()


# Display summary statistics in a row of metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")


st.subheader("Stats")
st.write(books_df.head())


col1, col2 = st.columns(2)


with col1:
    st.subheader("top 10 book titles")
    top_title = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_title)


with col2:
    st.subheader("Top 10 authors")
    top_authors = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig = px.pie(books_df,names="Genre",title='Most liked Genre 2009-2022', color="Genre",
color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Top 15 Authors")
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns=['Author','Count']

figg = px.bar(top_authors, x="Count", y="Author",orientation="h",
              title='Top 15 authors',
              labels={'Count': 'Counts of Books Published','Author':'Author'},
              color='Count', color_continuous_scale=px.colors.sequential.Plasma
              )
st.plotly_chart(figg)