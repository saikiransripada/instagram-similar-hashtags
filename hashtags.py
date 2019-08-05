import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/web/search/topsearch/?context=blended&query=%23'
search_tag = str(input('Please enter the hashtag you would like to search: '))

if '#' in search_tag:
    search_tag = search_tag.strip('#')

r = requests.get(url + search_tag)
response = r.json()['hashtags']

for data in response:
    print(f"#{data['hashtag']['name']}")