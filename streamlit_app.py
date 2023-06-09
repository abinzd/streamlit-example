from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_url = request.form['product_url']
        website_choice = int(request.form['website_choice'])

        if website_choice == 1:
            product_price = get_product_price_amazon(product_url)
            return render_template('result.html', price=product_price, website='Amazon')
        elif website_choice == 2:
            product_price = get_product_price_flipkart(product_url)
            return render_template('result.html', price=product_price, website='Flipkart')
        else:
            return "Invalid choice. Please try again."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
