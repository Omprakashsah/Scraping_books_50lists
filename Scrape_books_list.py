import time

import requests as re
from bs4 import BeautifulSoup as bs

#Get the URL and Send the URL:
url = 'https://books.toscrape.com/'
response = re.get(url)
if response.status_code == 200:
    print("Successful Request")
else:
    print("Request Failed!")

#Create a Soup object to parse the html content
soup = bs(response.text, 'html.parser')
print(soup)

#Find the titles and their links
books = soup.find_all('h3')
stat_time = time.time()
books_extracted = 0

#Itrating through the books and extracting their information
for book in books:
    book_url = book.find('a')['href']
    book_response = re.get(url + book_url)
    book_soup = bs(book_response.content, 'html.parser')

    title = book_soup.find('h1').text
    category = book_soup.find('ul', class_='breadcrumb').find_all('a')[2].text.strip()
    rating = book_soup.find('p', class_='star-rating')['class'][1]
    price = book_soup.find('p', class_= 'price_color').text.strip()
    availability = book_soup.find('p', class_='availability').text.strip()


    print(f'Title of the book: {title}')
    print(f'this is a {category} based book')
    print(f'Rating of the book is: {rating}')
    print(f'The price of the book is: {price}')
    print(f'This book is {availability}')
    print('____***___')


    books_extracted += 1
    end_time = time.time()
    total_time = (end_time-stat_time)/60.00
