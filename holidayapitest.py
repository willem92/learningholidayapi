from setuptools import setup
import holidayapi
import json
import requests

hapi = holidayapi.v1('bf83c323-3af7-41b9-b3e3-df9f6562f915')

parameters = {
    # Required
    'country': 'DE',
    'year':    2024,
    # Optional
    # 'month':    7,
    # 'day':      4,
    # 'previous': True,
    # 'upcoming': True,
    # 'public':   True,
    'pretty':   True

}

holidays = hapi.holidays(parameters)

#API Request
response = requests.get("https://holidayapi.com/v1/holidays", params={"country": "DE, AD, AE, AF, AG, AI, AL, AM, AO, AR,", "year": 2024, "key": "bf83c323-3af7-41b9-b3e3-df9f6562f915"})
data = response.json()

#Daten der feiertage
holidays = data['holidays']

#Sortieren nach Land
sorted_holidays = sorted(holidays, key=lambda x: x['country'])

#Ausgabe der sortierten Feiertage
for holiday in sorted_holidays:
    print(f"{holiday['country']} - {holiday['date']} - {holiday['name']}")