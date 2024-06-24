import requests
from bs4 import BeautifulSoup

# sample menu from the restaurant i had eaten food from
url = ""
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

menu_items = []
for item in soup.find_all('div', class_='menu-item'):
    name = item.find('h4').text.strip()
    description = item.find('p').text.strip()
    price = item.find('span', class_='menu-item-price').text.strip()
    menu_items.append({'name': name, 'description': description, 'price': price})

for item in menu_items:
    print(item)