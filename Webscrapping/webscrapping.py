import requests
from bs4 import BeautifulSoup

#r = requests.get("http://www.pythonhow.com/example.html")
#r = requests.get("http://www.pyclass.com/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

r=requests.get("http://www.pyclass.com/example.html")
c=r.content
r