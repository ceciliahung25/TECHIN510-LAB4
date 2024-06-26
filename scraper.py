import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from db import Database
import os

def convert_rating_to_number(rating_word):
    rating_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    return rating_map.get(rating_word)

def scrape_books():
    base_url = 'http://books.toscrape.com/catalogue/'
    start_url = 'page-1.html'
    next_url = start_url

    # Initialize the database and ensure the table exists
    with Database(os.getenv('DATABASE_URL')) as db:
        db.create_books_table()  # Create the table if it doesn't exist

        while next_url:
            full_url = urljoin(base_url, next_url)
            response = requests.get(full_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('article', class_='product_pod')

            for article in articles:
                title = article.find('h3').find('a')['title']
                price_text = article.find('p', class_='price_color').text
                price = float(price_text[1:])
                rating_word = article.find('p', class_='star-rating')['class'][1]
                rating = convert_rating_to_number(rating_word)
                link = article.find('h3').find('a')['href']
                details_url = urljoin(full_url, link)
                details_response = requests.get(details_url)
                details_soup = BeautifulSoup(details_response.content, 'html.parser')
                description = details_soup.find('meta', attrs={'name': 'description'})['content'].strip()

                book = {
                    'title': title,
                    'description': description,
                    'price': price,
                    'rating': rating
                }
                
                db.insert_book(book)

            next_link = soup.find('li', class_='next')
            next_url = next_link.find('a')['href'] if next_link else None

if __name__ == '__main__':
    scrape_books()


