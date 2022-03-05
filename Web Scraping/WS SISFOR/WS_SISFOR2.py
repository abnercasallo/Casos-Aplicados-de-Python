# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:24:28 2020

@author: abner
"""

from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

######
DRIVER_PATH = 'C:/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://observatorio.osinfor.gob.pe/Observatorio/Home/listaRoja")
driver.find_element_by_xpath("//img[@src='/Observatorio/Imagenes/iconos/map_sisfor.png']").click()

######REUBICAMOS EL WEB DRIVER A LA NUEVA VENTANA
window_after = driver.window_handles[1] ###Ubicación 1 pues es la ventana 2
driver.switch_to.window(window_after)
driver.find_element_by_css_selector("span.fa.fa-download").click()
#poner delay 
########REUBICAMOS NUEVAMENTE PARA EXTRAER LA VENTANA PDF#####
window_after = driver.window_handles[2]  ###Ubicación 2, pues es la ventana 3
driver.switch_to.window(window_after)
urlwd=driver.current_url
#print(urlwd)
print(urlwd)
#########EXTRACCIÓN##############
#import io
#import requests
#import PyPDF2
#from PyPDF2 import PdfFileReader

#pip3 install PyPDF2
#python -m pip install PyPDF
#r = requests.get(urlwd)
#f = io.BytesIO(r.content)

#reader = PdfFileReader(f)
#contents1 = reader.getPage(0).extractText() #pag1, podría usarse .split('\n')
#contents2 = reader.getPage(1).extractText() #pag2, podría usarse .split('\n')
#print(contents1)
#print(contents2)
#contents1 = reader.getPage(0).extractText()
#Text=contents1+contents2
#print(Text)

#type(contents1)
#import re
#xx = "guru99,education is fun"
#r1 = re.findall("[a-z]+",contents1)
#print(r1)

#patron="Tornillo(.*?)Fecha de Ingreso al Observatorio"##Es mejor tener la data precisa, para evitar dobles lecturas
#substring = re.search(patron, Text).group(0)
#print(substring)
#####AGRUPAMOS
#patron_tornillo="Tornillo(.*?)Fuente:"
#patron_tornillo1="Tornillo(.*?)%"
#substring_tornillo1 = re.search(patron_tornillo1, substring).group(1)
#patron_tornillo2="%(.*?)%"
#substring_tornillo2 = re.search(patron_tornillo2, substring).group(0)
#print(substring_tornillo1)
#print(substring_tornillo2)

###########FORMAMOS BASES DE DATOS#############

####PARA LAS QUE TENGAN 2 FILAS EN LA PRIMERA PÁGINA Y 3 EN LA SEGUNDA
#Usamos la función read_pdf del módulo "tabula", que lee df de pdfs web
###pag.1
from tabula import read_pdf
try: 
    df1=read_pdf(urlwd, pages=1)
    print(df1)
except Exception as e:
    print(e)

###pag.2
try: 
    df2=read_pdf(urlwd, pages=2)
    print(df2)
except Exception as e:
    print(e)
    
###Trabajando con la pág 1
print(type(df1))  ###Es una lista
df1=df1[0]
print(type(df1))  #Es un dataframe
##Conclusión:ERA UNA LISTA QUE CONTENÍA DATA FRAMES

##Trabajando la base de datos con la pag 2 
df2=df2[0]   #nuevamente, es una lista de df, escogemos el df
#la lista de datos está como encabezado, la extraemos:
df2=list(df2.columns.values)  ###header, forma simplificadda: (df3) 

#Juntamos
import pandas as pd
df2= pd.DataFrame(df2) 
df2=df2.transpose()
df_final=pd.concat([df1,df2],axis=0)

df1.to_excel('D:\\df1.xlsx', index = True)
df2.to_excel('D:\\df2.xlsx', index = True)
df_final.to_excel('D:\\df_final.xlsx', index = True)




#df_final = pd.DataFrame() 
#for i in range(0,8):
#    p=pd.DataFrame(df_pag1.iloc[i,])
#    q=p.transpose()
#    df_final=df_final.append(q)

#Ahora juntamos la página 2 con la 1
#df_final=df_final.append(df_pag2)




