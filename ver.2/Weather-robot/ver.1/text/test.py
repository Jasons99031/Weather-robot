import requests
import json

date ='2005-01-01'

def Req(date):

    url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467110&stname=%25E9%2587%2591%25E9%2596%2580&datepicker=' 
    CSV_URL = url+date
    #print(CSV_URL)

    with requests.Session() as s: #下載HTML
        download = s.get(CSV_URL) 
        #print(download.text)
        content=download.text

    with open("test.txt",'w') as f:#將資料存在筆記本
        f.write(content)

'''
將下載下來的HTML整理

'''


import bs4

with open('test.txt','r') as file:
    root = bs4.BeautifulSoup(file, "html.parser")
    
    print(root.tbody.tr.td)

#Req(date)




