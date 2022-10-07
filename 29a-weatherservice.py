import requests


class WeatherService:
    baseUrl = 'https://api.openweathermap.org/data/2.5'
    appId = '18fe102b63df96ae75952f0868ce7c05'

    @classmethod
    def getForecast(cls, city='omaha', country='us'):
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
