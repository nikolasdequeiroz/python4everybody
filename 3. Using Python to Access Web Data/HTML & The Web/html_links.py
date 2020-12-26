import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for i in range(count):
    link = tags[position].get('href', None)
    print(tags[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')