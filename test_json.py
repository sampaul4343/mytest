import urllib.request as urllib
import json

response = urllib.urlopen('https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json')

for data in json.load(response):
    print('{County}{SiteName}: {AQI}'.format(**data))
