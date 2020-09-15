#pulls urls from csv and gets the title from the page for each product

import requests
from bs4 import BeautifulSoup
from csv import reader
import pandas as pd

urls = []
titles = []

with open('bookslinks.csv', 'r') as f:
    csv_reader = reader(f)
    for row in csv_reader:
        urls.append(row[0])

def transform(url):
    r = requests.get(str(url))
    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.find('h1').text
    titles.append(title)
    print(title)
    return 

for url in urls:
    transform(url)

print(len(titles))

df = pd.DataFrame(titles)
df.to_csv('standard-booktitles.csv', index=False)
print('Complete.')
