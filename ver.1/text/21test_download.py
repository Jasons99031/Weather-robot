

import urllib.request as req

url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467110&stname=%25E9%2587%2591%25E9%2596%2580&datepicker=2010-01-01'



request = req.Request(url,headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
})


with req.urlopen(url) as response:
    data=response.read().decode("utf-8")
print(data)



'''
import requests 


with requests.Session() as s: #下載HTML
    download = s.get(url) 
print(download.text)
#with open("A.HTML","w") as S:
   # S.write(S)

'''


