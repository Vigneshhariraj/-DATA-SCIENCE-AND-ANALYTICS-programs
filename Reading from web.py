''' pip install lxml 
 pip install html5lib 
 pip install bs4'''
import pandas as pd 
url="https://en.wikipedia.org/wiki/Iris_flower_data_set" 
df=pd.read_html(url) 
print(df)