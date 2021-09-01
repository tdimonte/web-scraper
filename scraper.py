from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://us.theoodie.com/"

request = urlopen(url)
page_html = request.read()
request.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

items = html_soup.find_all('div', class_="grid-view-item")

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Title, Price, SalePrice \n'

f.write(headers)

#loop not working :/
for val in items:
    title = val.find('div', class_="h4 grid-view-item__title").text
    price = val.find('span', class_="product-price__price").text
    salePrice = val.find('span', class_="money").text

f.write(title + ',' + price + ',' + salePrice)

f.close()