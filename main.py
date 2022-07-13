#Scraping product prices from web in Azerbaijan marketplace

from bs4 import BeautifulSoup as BS
import requests 
import csv
from alive_progress import alive_bar

n=0
f= open("qiymetler.csv", "w",encoding="utf-8",newline='')  #All result will record to new csv file
writer = csv.writer(f)

#This is parent categories of products
with alive_bar(500) as bar:
    for mehsul_novu in ['meyve-terevez-quru-meyveler/meyve','meyve-terevez-quru-meyveler/goyerti','meyve-terevez-quru-meyveler/terevez','meyve-terevez-quru-meyveler/quru-meyve',
                        'et-toyuq-deniz-mehsullari/mal%20eti','et-toyuq-deniz-mehsullari/toyuq','et-toyuq-deniz-mehsullari/deniz-mehsullari',
                        'qastronom/dondurma','qastronom/kolbasa-sosisler','qastronom/donmus-mehsullar']:
        page=1
        dovr=True

        while dovr:
            url = 'https://neptun.az/'+mehsul_novu+'?page='+str(page)
            result=requests.get(url)
            soup=BS(result.text,'html.parser')
            print(url+"     |")

            if(len(soup.find_all("div", class_="caption"))):
                for tags in soup.find_all("div", class_="caption"):
                    try:
                        n+=1
                        row=str(n), tags.find("h4").text, tags.find("span",class_="price-new").string, mehsul_novu
                        writer.writerow(row)
                    except:
                        print(row+(' yaza bilmedi',))    
                    bar()
                page+=1 
            else:
                dovr=False
print(str(n)+" sayda mehsul yazildi!")  #Little report after execution
f.close
