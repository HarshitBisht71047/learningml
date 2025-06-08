import pandas as pd
import requests

url= "https://jsonplaceholder.typicode.com/posts"

response= requests.get(url)
temp_df=pd.DataFrame(response.json())

if response.status_code==200:
    df=pd.DataFrame(temp_df)
    print('Data fetched')
    df.to_csv("api.csv",index=False)

else:
    print('Error')

    