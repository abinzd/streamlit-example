import streamlit as st
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

def main():
    st.title("Price Checker")
    st.write("Welcome to the Price Checker!")
    product_url = st.text_input("Enter the URL of the product:")
    website_choice = st.selectbox("Select the website:", ['Amazon', 'Flipkart'])

    if st.button("Check Price"):
        if website_choice == 'Amazon':
            product_price = get_product_price_amazon(product_url)
            st.write('Amazon Price:', product_price)
        elif website_choice == 'Flipkart':
            product_price = get_product_price_flipkart(product_url)
            st.write('Flipkart Price:', product_price)
        else:
            st.write('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
