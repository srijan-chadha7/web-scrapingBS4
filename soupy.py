import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter - ')
#req=Request(url,headers={'User-Agent':'Mozilla/5.0'})
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

#containers=soup.findAll("div",{"class":"citySelectionWrapper"})
tags=soup.findAll('a')
#print(tag.get_text())
#tags=soup('div')
for tag in tags:
    #tag1=tag.find('div', class_ = 'restaurant-name closed')
    print(tag.text)
