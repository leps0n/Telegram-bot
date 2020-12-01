import requests
from bs4 import BeautifulSoup

URL_weather = 'https://www.gismeteo.by/weather-minsk-4248/'
URL_teacher = 'https://journal.bsuir.by/api/v1/employees'
# URL_schedule = 'https://iis.bsuir.by/schedule;groupName'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.77 YaBrowser/20.11.0.817 Yowser/2.5 Safari/537.36'}
def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

def get_weather(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find('div', class_='date').get_text(strip=True)
    time = soup.find('div', class_='date xs fadeIn').get_text(strip=True)
    temp = soup.find('span', class_='js_value tab-weather__value_l').get_text(strip=True)
    r='Дата: '+data+'\nВремя: '+time+'\nТемпература: '+temp
    return r

def get_teacher(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='con').find_all('span')
    print(items)

def parse():
    global str
    html_weather = get_html(URL_weather)
    if html_weather.status_code == 200:
        str=get_weather(html_weather.text)
        return str
    else:
        print('error')

parse()