#Environment Setup (Python and pip paths)
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_test = "https://us.theoodie.com/"

request = urlopen(url_test)
page_html = request.read()
request.close()