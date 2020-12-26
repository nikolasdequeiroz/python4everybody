import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
sum_page = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    number = (re.findall(r"[0-9]+", tag.decode()))
    print(number)

    for n in number:
        n = int(n)
        sum_page = n + sum_page

print(sum_page)