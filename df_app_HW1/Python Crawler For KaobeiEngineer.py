import requests
from bs4 import BeautifulSoup

url = 'https://kaobei.engineer/rankings/'
tag = '.col-block a img'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

index = 0
for img in soup.select(tag):
    index += 1
    img_data = requests.get(img.get('src')).content
    with open('./data/quarterlyTop/quarterlyTop_{}.jpg'.format(index), 'wb') as handler:
        handler.write(img_data)