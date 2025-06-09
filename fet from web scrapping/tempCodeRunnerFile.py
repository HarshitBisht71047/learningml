import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup

url= "https://musclenectar.com/collections/products"

response= requests.get(url).text
soup= BeautifulSoup(response,'lxml')

print(soup.find('h1').text)
