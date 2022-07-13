import requests
from time import sleep
from bs4 import BeautifulSoup

for j in range(1,5): 
   r=requests.get('https://turbo.az/autos')
   soup=BeautifulSoup(r.text,'html.parser')

   #sonelan=soup.find_all("p",string="ELANLAR")

   #Lazimi taglar parse edilib oxunur
   ad=soup.find_all('div',attrs={'class':'products-i__name'})
   qiymet=soup.find_all('div',attrs={'class':'product-price'})
   atributlar=soup.find_all('div',attrs={'class':'products-i__attributes'})
   tarix=soup.find_all('div',attrs={'class':'products-i__datetime'})

   #Atributlar cap edilir
   file_yaz=open("TestIO/turboyaz.txt", "a")
   a=int(len(qiymet))
   for i in range(1,a):  
     file_yaz.write(ad[i].text+'\n');
     file_yaz.write(qiymet[i].text+'\n');
     file_yaz.write(atributlar[i].text+'\n');
     file_yaz.write(tarix[i].text+'\n');
     file_yaz.write('-----------------------'+'\n');

   print(str(i)+" yeni elan elave edildi.")
   sleep(200)
