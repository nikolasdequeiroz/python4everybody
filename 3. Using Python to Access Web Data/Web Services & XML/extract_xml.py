import xml.etree.ElementTree as ET
import urllib.request

url = input("Enter location: ")

xml = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml)
tags_list = tree.findall('.//count')
sum_counts = 0

for tag in tags_list:
    sum_counts = sum_counts + int(tag.text)

print(sum_counts)
