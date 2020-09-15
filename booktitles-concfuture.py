import pandas as pd
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from csv import reader

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

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(transform, urls)

print(len(titles))
df = pd.DataFrame(titles)
df.to_csv('concurrent-titles.csv', index=False)
print('Complete.')
