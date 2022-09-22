# weatherService.py

import requests


class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5'
    appId = '51806f9856e05e80f6f68a1f013bc92b'

    @classmethod
    def getForecast(cls, city="new york", country="us"):
        url = f'{cls.baseUrl}/forecast'

        response = requests.get(url, params=[
            ('q', f'{city},{country}'),
            ('mode', 'json'),
            ('APPID', cls.appId)
        ])

        data = response.json()

        return data['list']


if __name__ == "__main__":
    print(WeatherService.getForecast())
