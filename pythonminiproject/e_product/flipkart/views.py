from django.shortcuts import render
import  re
from django.shortcuts import get_object_or_404, get_list_or_404
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

from product.models import Product

product_details = {}


def generate_key():
    value = 0
    while True:
        value += 1
        yield value


ids = generate_key()


def crawl_flipkart(product: str, value: int):
    start_url = 'https://www.flipkart.com/search?' + urlencode(
        {'q': product}) + '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page=%s'

    urls = [start_url.replace('%s', str(page)) for page in range(0, value + 1)]

    for url in urls:
        print('1: ', url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        product_titles = soup.find_all('div', class_='_4rR01T')
        product_price = soup.find_all('div', class_='_3I9_wc _27UcVY')
        product_offer = soup.find_all('div', class_='_3Ay6Sb')
        product_offer_price = soup.find_all('div', class_='_30jeq3 _1_WHN1')
        product_url = soup.find_all('div', class_='_2kHMtA')
        product_data = soup.find_all('a', class_='_1fQZEK')

        for i in zip(product_titles, product_price, product_offer, product_offer_price, product_url, product_data):
            product_name = i[0].text
            name = re.sub("\(.*?\)","()", product_name)
            product_details[next(ids)] = {'name': name.replace('()', ''), 'original_price': i[1].text.replace('₹', '').replace(',', '.'),
                                          'offer_%': i[2].text.replace('off', '').replace('%', ''),
                                          'offer_price': i[3].text.replace('₹', ''), 'product_url': i[5].get("href")}

            product = get_object_or_404(Product, name=name.replace('()', ''), is_active=True)
            request = {'product': product.id, 'shop': 1,
                       'actual_price': i[1].text.replace('₹', '').replace(',', '.'),
                       'offer_percentage': i[2].text.replace('off', '').replace('%', ''),
                       'vendor_price': i[3].text.replace('₹', '').replace(',', '.'),
                       'product_url': i[5].get("href"),
                       'user_id': 1}

            return request


def print_details():
    for values in product_details.values():
        print(values.get('name'))
        print(values.get('original_price'))
        print(values.get('offer_%'))
        print(values.get('offer_price'))
        print(f'https://www.flipkart.com{values.get("product_url")}')



if __name__ == "__main__":
    is_continue = True
    while is_continue:
        user_choice = int(input('Enter 1 to scrawl data/nEnter 2 to display scrawled data: '))
        match user_choice:
            case 1:
                crawl_flipkart('oneplus Nord Ce 2 5G', 3)

            case 2:
                print_details()

            case 3:
                is_continue = False


