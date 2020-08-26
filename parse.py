import requests

from bs4 import BeautifulSoup

URL = 'https://auto.ru/moskva/cars/kia/new/'
HEADERS = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                         '84.0.4147.135 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='Link')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='ListingItem-module__columnCellSummary').get_text()
        })
    print(cars)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
