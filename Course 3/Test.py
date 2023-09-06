import urllib.request
import json

url = input("Enter the URL:")

info = json.loads(urllib.request.urlopen(url).read())

x = 0
count=0
for items in info['comments']:
    x= x + int(items['count'])
    count = count + 1
print ('Count ',(count))
print ('Sum : ',(x))
