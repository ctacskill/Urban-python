import requests

params = {
    "latitude": 52.2978,
    "longitude": 104.296,
    "daily": 'temperature_2m_min,temperature_2m_max',
    "timezone": "Asia/Irkutsk"}

url = 'https://api.open-meteo.com/v1/forecast'

def temperature_v_irkutske():
    response_ = requests.get(url, params=params)
    data = response_.json()
    date = data['daily']['time'][0]
    min_temp = data['daily']['temperature_2m_min'][0]
    max_temp = data['daily']['temperature_2m_max'][0]
    print(f'дата: {date}')
    print(f'Минимальная температура: {min_temp}')
    print(f'Максимальная температура: {max_temp}')
temperature_v_irkutske()




import pandas as pd
import openpyxl

df = pd.read_excel('тест.xlsx')
print(df)


