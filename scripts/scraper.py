import requests
from bs4 import BeautifulSoup

URL = "https://www.davidson.edu/"

def get_html(url):
    response = requests.get(url)
    return response.text    

def get_links(soup):
    # links = []
    # for link in soup.find_all('a'):
        # links.append(link.get('href'))
    # return links

    return soup.find_all('a')

def get_metatags(soup):
    metatags = []
    for metatag in soup.find_all('meta'):
        metatags.append(metatag)
    return metatags


soup = BeautifulSoup(get_html(URL), 'html.parser')

# printing link tags
for link in get_links(soup):
    print(link)

print("\n======================================\n")

# printings meta tags
for metatag in get_metatags(soup):
    print(metatag)