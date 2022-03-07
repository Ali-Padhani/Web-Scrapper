from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

import re 

driver = webdriver.Chrome("C:\Program Files\Java\chromedriver")

Baseurl =  "https://simpletire.com/"
Brand = "tire-brands"
accelera = "achilles"
tire = "-tires/"
driver.get(Baseurl+Brand)

content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")

brandname = []
brandURL = []

for div in soup.find_all('div', attrs={'class':'col-md-3 col-sm-4'}):
    
    for a in div.find_all('a', href=True):
        print('{} - {}'.format(a.get_text(strip=True), a['href']))
        brandname.append(a.get_text(strip=True))
        brandURL.append(a['href'])
""" 
for a in soup.findAll('a',href=True, attrs={'class':'index-a'}):
    print(a)
    names.append(a)


"""
print ("NAmes: ",brandname)
print ("NAmes: ",brandURL)

#name_lower = list(map(to_lover_case,names))
driver.close()
