import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = 'https://www.otomoto.pl/osobowe/od-2015?search%5Bfilter_float_price%3Ato%5D=20000&search%5Border%5D=filter_float_price%3Adesc'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
cars = soup.find_all('article')

wb = Workbook()
ws = wb.active

ws.append(['Name', 'Price', 'URL'])

for car in cars:
    title_tag = car.find('a')
    price_tag = car.find('h3')

    if title_tag and price_tag:
        title = title_tag.text.strip()
        car_url = title_tag['href']
        price = price_tag.text.strip()
        ws.append([title, price, car_url])



wb.save('cars.xlsx')

print("✅ File \"cars.xlsx\" is created")

