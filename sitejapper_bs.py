from bs4 import BeautifulSoup
import requests
import csv
import re


f = open('FILE DESTINATION', 'w')
w = csv.writer(f)
w.writerow(['Date', 'Stars', 'Comment'])

pages = []

# This appends all the pages for Sitejabber's Uber reviews to pages.
for i in range(1, 33):
    url = 'https://www.sitejabber.com/reviews/uber.com?page=' + str(i) + '#reviews'
    pages.append(url)

for page in pages:
    # Gathering the html source code from the page
    source = requests.get(page).text

    soup = BeautifulSoup(source, 'lxml')
    
    # Find all reviews in the page
    reviews = soup.find_all('div', id=re.compile('^ReviewRow'))

    for review in reviews:
        # Comment of review
        comment = review.find('div', id=re.compile('^ReviewText')).text
        # Removing non-letters/formating
        comment = comment.replace("\t", "")
        comment = comment.replace("\n", "")
        
        # Date of review
        date = review.find('div', class_='time tiny_text faded_text').text
        # Removing non-letters/formating
        date = date.replace("\t", "")
        date = date.replace("\n", "")

        # Star rating of review
        stars = review.find('div', id=re.compile('^ReviewText')).get('data-rating')

        # Writing to csv file
        w.writerow([date, stars, comment])

f.close()
