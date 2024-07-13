import requests
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.accuweather.com/en/qa/doha/271669/hourly-weather-forecast/271669'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)
soup=BeautifulSoup(response.content,'lxml')

weather_dict={
    'Time':[],
    'Temp':[],
}

def get_weather():
    print('DOHA WEATHER APP')
    try:
        all_weather=soup.find_all('div',class_='hourly-card-top')
        for weather in all_weather:
            time_intervels=weather.find_all('h2',class_='date')
        
            for time in time_intervels:
                weather_dict['Time'].append(time.div.text)
        
            temps=weather.find_all('div',class_='temp')
            for temp in temps:
                formatted_temp=temp.text[0:2] #slicing of the ° symbol at the end of the temp
                weather_dict['Temp'].append(formatted_temp)
    
        df=pd.DataFrame(weather_dict)
        df.to_csv('weather.csv',sep='\t',index=False)   
        weather_info = pd.read_csv('weather.csv', sep='\t')
        min_temp=weather_info['Temp'].min()
        max_temp=weather_info['Temp'].max()
        print(f'\nMaximum Temperature:{max_temp}° C \nMinimum Temperature : {min_temp}° C\n')
        print(weather_info)
    except FileNotFoundError:
        print('no file')
    except Exception as e:
        print(e)

    
get_weather()
