import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter URL: ")

data = urllib.request.urlopen(url).read()
info = json.loads(data)

sum_counts = 0

for usr in info['comments']:
    sum_counts = sum_counts + int(usr['count'])

print(sum_counts)