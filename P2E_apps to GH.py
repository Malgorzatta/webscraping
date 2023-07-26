import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

pages = np.arange(1,2)
headers = []
row_data = []

for page in pages:
    url = "https://playtoearn.net/blockchaingames?sort=name&direction=asc&page="+str(page)+""
    #print(url)
    page = requests.get(url)
    #print(page)
    soup = BeautifulSoup(page.text, 'lxml')
    #print(soup)

    table1 = soup.find("table",{"class":"table table-bordered mainlist"})

    for y in table1.find_all('tr')[1:]:
        second_td = y.find_all('td')[3].find_all('a')
        #print(second_td)
        #second_tdA = [a.text.strip() for a in second_td]
        #if 'Move-To-Earn' not in second_tdA:
        #    continue
        #print(second_tdA)
        
        blockchains = []
        for third_td in y.find_all('td')[4].find_all('a'):
            blockchain = third_td['title']
            blockchains.append(blockchain)
        #print(blockchains)

        td_tags = y.find_all('td')
        #print(td_tags)

        devices = []
        for fourth_td in y.find_all('td')[5].find_all('a'):
            device = fourth_td['title']
            devices.append(device)
        print(devices)
        row = [z.text.strip() for z in td_tags]
        row_data.append(row)
        print(row)

for x in table1.find_all('th'):
    title = x.text
    title=title.strip()
    headers.append(title)
#print(headers)

mydata = pd.DataFrame(row_data, columns = headers)
mydata.drop('', inplace=True, axis=1)
mydata.drop('Social 7d', inplace=True, axis=1)
mydata.drop('Social 24h', inplace=True, axis=1)

print(mydata)
