import requests
from bs4 import BeautifulSoup
import re
import json

canon=[]
for i in range(155):
    url="http://www.cavafy.com/poems/content.asp?cat=1&id="+str(i)
    response = requests.get(url)

    htmlContent = response.text

    #print(htmlContent)

    soup = BeautifulSoup(htmlContent, 'lxml')
    td= soup.find_all('td')
    convertedstr = str(td[33])


    #print(convertedstr)
    #tmp=[]
    rep = {'<br/>':'\n','\r\n':'', '\xa0':'', '<td>':'', '</td>':'','\x97':'','\x92':''}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    text = pattern.sub(lambda m: rep[re.escape(m.group(0))], convertedstr)
    
    canon.append({'id':i,'poem':text})

with open('cav.json','w') as outfile:
    json.dump(canon, outfile, indent=2)

#dataJson = [{'id':}]
'''
count = 0
for i in td:
    count+=1
    print(count)
    print(i)
'''