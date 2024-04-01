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

books_data = []
#loop through all 50 pages
for page_num in range(1,51):
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    response = re.get(url)
    soup = bs(response.content, 'html.parser')

    # Find the titles and their links
    books = soup.find_all('h3')
    stat_time = time.time()
    books_extracted = 0

#adding the extracted info to the list:
for book in books:
    book_url = book.find('a')['href']
    book_response = re.get('https://books.toscrape.com/catalogue/' + book_url)
    book_soup = bs(book_response.content, 'html.parser')

    title = book_soup.find('h1').text
    category = book_soup.find('ul', class_='breadcrumb').find_all('a')[2].text.strip()
    rating = book_soup.find('p', class_='star-rating')['class'][1]
    price = book_soup.find('p', class_= 'price_color').text.strip()
    availability = book_soup.find('p', class_='availability').text.strip()

    end_time = time.time()
    total_time = (end_time-stat_time)/60.00

    books_data.append([title, category, rating, price, availability])
    print(books_data)
    print("___END___")

    print(f'Total time taken to extract: {total_time:.2f} min')
    print("___***___")

    print(f'{page_num * len(books)} books extracted...')


