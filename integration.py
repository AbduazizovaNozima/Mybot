
# import requests
# from pprint import pprint

# API_KEY = '88128bf4faf110cc7acd2f787a359263'

# def get_weather_data(city):
#     weather_feeling = {
#         'Clear': 'Ochiq havo🌞',
#         'Clouds': 'Bulutli☁️',
#         'Rain': "Yomgirli🌧",
#         'Mist': 'Tuman💨'
#     }

#     response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}')
#     data = response.json()

#     humidity = data['main']['humidity']
#     temp = round(data['main']['temp'] - 273.15, 2)
#     weather = weather_feeling.get(data['weather'][0]['main'])
#     wind = data ['wind']['speed']
#     message = f"""
#     Ob-xavo ma'lumotlari: \nTemperatura:{temp} 
#     \nNamlik:{humidity} \nHolati:{weather} 
#     \nShamol tezligi{wind}"""

#     return message

import requests

API_KEY = '71b986edd89bbee36cefb5aa'

def get_UZS(usd_amount):

    url = f"https://v6.exchangerate-api.com/v6/71b986edd89bbee36cefb5aa/latest/USD"

    response = requests.get(url)
    data = response.json()

    sum_to_usd = data['conversion_rates']['UZS']

    uzs_amount = usd_amount * sum_to_usd


    message = f"{usd_amount} USD ning hozirgi qiymati {uzs_amount} UZS."
    return message




