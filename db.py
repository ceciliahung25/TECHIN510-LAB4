import psycopg2

class Database:
    def __init__(self, database_url):
        self.con = psycopg2.connect(database_url)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.con.close()

    def create_books_table(self):
        # SQL command to create a table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            description TEXT,
            price NUMERIC(6,2),  -- Assumes price has at most 6 digits, 2 of which are after the decimal point
            rating INTEGER       -- Assumes rating is an integer
        );
        """
        self.cur.execute(create_table_query)
        self.con.commit()

    def insert_book(self, book):
        # SQL command to insert a new row into the books table
        q = """
        INSERT INTO books (title, description, price, rating) VALUES (%s, %s, %s, %s)
        """
        self.cur.execute(q, (book['title'], book['description'], book['price'], book['rating']))
        self.con.commit()
