# Import necessary libraries
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from db import Database

# Load environment variables from .env file
load_dotenv()

# Retrieve the DATABASE_URL from the environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

class Database:
    def __init__(self, database_url):
        import psycopg2
        self.con = psycopg2.connect(database_url)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.con.close()

    def fetch_books(self, search_query="", rating_filter=None, order_by=""):
        query = f"SELECT * FROM books WHERE title ILIKE '%{search_query}%' OR description ILIKE '%{search_query}%'"
        if rating_filter:
            query += f" AND rating = {rating_filter}"
        if order_by:
            query += f" ORDER BY {order_by}"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return pd.DataFrame(rows, columns=['id', 'title', 'description', 'price', 'rating'])

def main():
    st.title('Book Explorer')
    search_query = st.text_input("Search by Book Title or Description")
    rating_filter = st.selectbox("Filter by Rating", ('', '1', '2', '3', '4', '5'), index=0)
    order_by = st.selectbox("Order By", ('', 'price', 'rating'), index=0)

    if st.button('Fetch Books'):
        with Database(DATABASE_URL) as db:
            books = db.fetch_books(search_query, rating_filter, order_by if order_by else None)
            if books.empty:
                st.write("No books found. Please refine your search criteria.")
            else:
                st.write(f"Found {len(books)} books:")
                st.dataframe(books)

if __name__ == '__main__':
    main()

