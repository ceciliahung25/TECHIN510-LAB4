import os
import requests
from bs4 import BeautifulSoup
from db import Database
from urllib.parse import urljoin, urlparse

def scrape_books():
    base_url = 'http://books.toscrape.com/catalogue/'
    start_url = 'page-1.html'
    next_url = start_url

    while next_url:
        full_url = urljoin(base_url, next_url)
        response = requests.get(full_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='product_pod')

        for article in articles:
            title = article.find('h3').find('a')['title']
            price = article.find('p', class_='price_color').text[1:]  # Remove currency symbol
            rating_word = article.find('p', class_='star-rating')['class'][1]
            rating = convert_rating_to_number(rating_word)  # Implement this function based on your rating system
            link = article.find('h3').find('a')['href']
            details_url = urljoin(full_url, link)
            details_response = requests.get(details_url)
            details_soup = BeautifulSoup(details_response.content, 'html.parser')
            description = details_soup.find('meta', attrs={'name': 'description'})['content'].strip()

            book = {'title': title, 'description': description, 'price': float(price), 'rating': rating}
            
            with Database(os.getenv('DATABASE_URL')) as db:
                db.insert_book(book)

        next_link = soup.find('li', class_='next')
        next_url = next_link.find('a')['href'] if next_link else None

def convert_rating_to_number(rating_word):
    rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    return rating_map.get(rating_word, 0)

if __name__ == '__main__':
    scrape_books()
