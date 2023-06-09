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

# Example usage for Amazon
amazon_product_url = 'https://www.amazon.com/dp/B07VGRJDFY/'
amazon_price = get_product_price_amazon(amazon_product_url)
print('Amazon Price:', amazon_price)

# Example usage for Flipkart
flipkart_product_url = 'https://www.flipkart.com/apple-iphone-12-pro-max-silver-256-gb/p/itm2643019ff84b2'
flipkart_price = get_product_price_flipkart(flipkart_product_url)
print('Flipkart Price:', flipkart_price)
