import requests
from bs4 import BeautifulSoup
import csv
import os

html = open("D:\\Learning_First\\GitHub\\Parsing python\\data\\111.html").read()
FILE = 'Files\\MyGames.csv'


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='gameListRowItem')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='gameListRowItemName').get_text(),
            #'link': item.find('a', class_='popup_menu_item2 tight').find_next('href').get_text()
            'hours': item.find('h5', class_='ellipsis hours_played').get_text(),
            #'uah_price': uah_price,
            #'city': item.find('svg', class_='svg_i16_pin').find_next('span').get_text(),
        })
    return cars


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Время'])
        for item in items:
            writer.writerow([item['title'], item['hours']])


def parse():
    cars = []
    cars.extend(get_content(html))
    save_file(cars, FILE)
    print(f'Получено {len(cars)} объектов')
    os.startfile(FILE)


parse()
