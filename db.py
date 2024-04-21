import psycopg2

class Database:
    def __init__(self, database_url) -> None:
        self.con = psycopg2.connect(database_url)
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()

    def create_books_table(self):
        q = """
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price TEXT NOT NULL,
            rating TEXT NOT NULL
        );
        """
        self.cur.execute(q)
        self.con.commit()

    def insert_book(self, book):
        q = """
        INSERT INTO books (title, description, price, rating) VALUES (%s, %s, %s, %s)
        """
        self.cur.execute(q, (book['title'], book['description'], book['price'], book['rating']))
        self.con.commit()
