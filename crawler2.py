import requests
from bs4 import BeautifulSoup

def web(page,WebUrl):
    if(page>0):
        url = WebYrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll(‘a’, {‘class’:’s-access-detail-page’}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get(‘href’)
            print(tet_2)
web(1,’https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp__all_mobiles')