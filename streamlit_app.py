import requests
from bs4 import BeautifulSoup

def get_product_price_amazon(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find(id='priceblock_ourprice')
    if price_element is not None:
        return price_element.get_text().strip()
    else:
        return 'Price not available'

def get_product_price_flipkart(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find(class_='_1vC4OE_2rQ-NK')
    if price_element is not None:
        return price_element.get_text().strip()
    else:
        return 'Price not available'

# User interface
print("Welcome to the Price Checker!")
print("Please enter the URL of the product:")

product_url = input()

print("Select the website:")
print("1. Amazon")
print("2. Flipkart")

website_choice = int(input())

if website_choice == 1:
    product_price = get_product_price_amazon(product_url)
    print('Amazon Price:', product_price)
elif website_choice == 2:
    product_price = get_product_price_flipkart(product_url)
    print('Flipkart Price:', product_price)
else:
    print('Invalid choice. Please try again.')

