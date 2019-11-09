from bs4 import BeautifulSoup
import requests
import csv
import re

f = open('C:/Users/jojo2/Documents/PythonProjects/Uber2/sitejabber_uber.csv', 'w')
w = csv.writer(f)
w.writerow(['Date', 'Stars', 'Comment'])




pages = []

for i in range(1, 33):
    url = 'https://www.sitejabber.com/reviews/uber.com?page=' + str(i) + '#reviews'
    pages.append(url)

for page in pages:
    source = requests.get(page).text

    soup = BeautifulSoup(source, 'lxml')

    reviews = soup.find_all('div', id=re.compile('^ReviewRow'))

    for review in reviews:
        comment = review.find('div', id=re.compile('^ReviewText')).text
        comment = comment.replace("\t", "")
        comment = comment.replace("\n", "")
        # print(comment)

        date = review.find('div', class_='time tiny_text faded_text').text
        date = date.replace("\t", "")
        date = date.replace("\n", "")
        # print(date)

        stars = review.find('div', id=re.compile('^ReviewText')).get('data-rating')
        # print(stars)

        # print()

        w.writerow([date, stars, comment])

f.close()
