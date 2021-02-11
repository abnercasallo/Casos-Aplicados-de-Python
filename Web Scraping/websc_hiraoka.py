# -*- coding: utf-8 -*-
"""
Abner Francisco Casallo Trauco
Spyder Editor

This is a temporary script file.
"""

#Primero hemos instalado request es el terminal
#Tmb beautiful soup:$ pip3 install beautifulsoup4
from bs4 import BeautifulSoup
import pandas as pd
import requests

    
URL = 'https://hiraoka.com.pe/tecnologia/computadoras/laptops'
page = requests.get(URL)
print(page)
soup = BeautifulSoup(page.content)
print(soup)
prices_t = soup.find_all('span', class_ = "price")
print(prices_t)
prices_text=[item.text for item in prices_t]
print(prices_text)


text2=[]
for i in prices_text:
    a=i.replace(',','')
    b=a.replace('S/ ','')
    c=b.replace('.00','')
    text2.append(c)

print(text2)
num_prices_1=[]
for a in text2:
    num_prices_1.append(int(a))
       
print(num_prices_1)

#AVERAGE:
total_pag1=0
for i in num_prices_1:
    total_pag1=total_pag1+i
print(total_pag1)

av_price_pag1=total_pag1/len(num_prices_1)
print(av_price_pag1)

#########AHORA HACER UN BUCLE PARA TODAS LAS PÁGINAS CON FOR
#prices_text=[]
prices=[]
for i in range(1,5):#1,2,3,4
    if i==1:
        URL = 'https://hiraoka.com.pe/tecnologia/computadoras/laptops'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        prices_t = soup.find_all('span', class_ = "price")
        prices_text=[item.text for item in prices_t]
        for i in prices_text:
                a=i.replace(',','')
                b=a.replace('S/ ','')
                c=b.replace('.00','')
                prices.append(int(c))
    else:
        a=str(i)
        URL = 'https://hiraoka.com.pe/tecnologia/computadoras/laptops'+'?p='+a
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        prices_t = soup.find_all('span', class_ = "price")
        prices_text=[item.text for item in prices_t]
        for i in prices_text:
            a=i.replace(',','')
            b=a.replace('S/ ','')
            c=b.replace('.00','')
            prices.append(int(c))


print(prices)

#ARMAMOS EL DATA FRAME
#df_11nov = pd.DataFrame(prices, columns =['Precios al 12/11/2020']) 
df = pd.DataFrame(prices, columns =['Precios al 17/11/2020'])
print(df)

total=0
for i in prices:
    total=total+i
print(total)
print(total/len(prices))   ####SALE MÁS DE 5000, RAZÓN: OUTLIERS(10 MIL, 15 MIL...)

df.to_csv(r'D:\GITHUB\Web-Scraping-de-lap-tops-con-Python\Data generada\17 de nov.csv',
                sep=';')


        
    
    
