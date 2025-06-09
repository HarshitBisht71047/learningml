import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup

url= "https://musclenectar.com/collections/products"

response= requests.get(url).text
soup= BeautifulSoup(response,'lxml')

products = soup.find_all('a', class_="product-item-meta__title")
reviews = soup.find_all(class_="jdgm-prev-badge__text")
prices=soup.find_all(class_="price price--highlight")

product_name=[]
review=[]
price=[]
old_price=[]

for p in products:
    product_name.append(p.text.strip())

for r in reviews:
    review.append(r.text.strip())

for i in prices:
    price.append(i.text.strip())

df = pd.DataFrame({
    'product': product_name,
    'reviews': review,
    'price': price
})


print(df)
df.to_csv("muscle_nectar.csv",index=False)