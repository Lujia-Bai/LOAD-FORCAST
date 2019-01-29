
# coding: utf-8

# In[1]:


import sys
path = "/anaconda3/lib/python3.6/site-packages"
sys.path.append(path)


# In[20]:


#2015-2017
import requests
import csv
from bs4 import BeautifulSoup
#需要pip install urllib.request两个包
import urllib.request

table = soup.find("table", {"class" : "sortable wikitable"})
for year in range(2015,2018):
    f = open('/Users/bailujia/Desktop/table'+str(year)+'.csv', 'w')
    csv_writer = csv.writer(f)
    DATE =""   
    TEMP =""

    for month in range(1,13):
        date = year*100 + month
        url = "http://www.tianqihoubao.com/lishi/huaian/month/"+str(date)+".html"
        page = urllib.request.urlopen(url)  
        soup = BeautifulSoup(page,"lxml")  
        page.close()  
        tables = soup.findAll('table')  
        tab = tables[0]  
        for tr in tab.findAll('tr'):  
            td  = tr.findAll('td')
            DATE = td[0].getText()
            TEMP = td[2].getText()
            csv_writer.writerow([DATE, TEMP])
    f.close()


# In[16]:


#2018
import requests
import csv
from bs4 import BeautifulSoup
#需要pip install urllib.request两个包
import urllib.request
year=2018
f = open('/Users/bailujia/Desktop/table'+str(year)+'.csv', 'w')
csv_writer = csv.writer(f)
DATE =""   
TEMP =""

for month in range(1,7):
    date = year*100 + month
    url = "http://www.tianqihoubao.com/lishi/huaian/month/"+str(date)+".html"
    page = urllib.request.urlopen(url)  
    soup = BeautifulSoup(page,'lxml')
    page.close()  
    tables = soup.findAll('table')  
    tab = tables[0]  
    for tr in tab.findAll('tr'):  
        td  = tr.findAll('td')
        DATE = td[0].getText()
        TEMP = td[2].getText()
        csv_writer.writerow([DATE, TEMP])
f.close()

