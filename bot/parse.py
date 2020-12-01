import requests
from bs4 import BeautifulSoup

URL_weather = 'https://www.gismeteo.by/weather-minsk-4248/'
URL_weather_2 = 'https://www.gismeteo.by/weather-minsk-4248/now/'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.817 Yowser/2.5 Safari/537.36'}
def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

def get_weather(html):
    soup = BeautifulSoup(html, 'html.parser')
    time = soup.find('div', class_='date xs fadeIn').get_text(strip=True)
    temp = soup.find('span', class_='js_value tab-weather__value_l').get_text(strip=True)
    r='Время: '+time+'\nТемпература: '+temp
    return r

def get_weather_2(html):
    soup = BeautifulSoup(html, 'html.parser')
    state = soup.find('span', class_='tip _top _center').get_text(strip=True)
    wind = soup.find('div', class_='nowinfo__value').get_text(strip=True)+' '+soup.find('div', class_='nowinfo__measure nowinfo__measure_wind').get_text(strip=True)
    r = '\nСостояние: '+state+'\nВетер: '+wind
    return r

def parse():
    global str
    html_weather = get_html(URL_weather)
    if html_weather.status_code == 200:
        str=get_weather(html_weather.text)
    else:
        print('error')

    html_weather_2 = get_html(URL_weather_2)
    if html_weather_2.status_code == 200:
        str = str + get_weather_2(html_weather_2.text)
        return str
    else:
        print('error')

parse()