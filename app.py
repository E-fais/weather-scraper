import requests
from bs4 import BeautifulSoup

url='https://www.accuweather.com/en/qa/doha/271669/hourly-weather-forecast/271669'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)
soup=BeautifulSoup(response.content,'lxml')

weather_dict={
    'time':[],
    'temp':[],
}

def get_weather():
    all_weather=soup.find_all('div',class_='hourly-card-top')
    for weather in all_weather:
        time_intervels=weather.find_all('h2',class_='date')
       
        for time in time_intervels:
            weather_dict['time'].append(time.div.text)
       
        temps=weather.find_all('div',class_='temp')
        for temp in temps:
            weather_dict['temp'].append(temp.text)
    print(weather_dict)
get_weather()
# print(weather_dict)