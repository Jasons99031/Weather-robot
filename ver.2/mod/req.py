import requests
import threading
from .arrange import arr


class Req(threading.Thread):
    def __init__(self,dete): 
        threading.Thread.__init__(self) #要用threading funtion 要叫run
        self.date=dete
        url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467110&stname=%25E9%2587%2591%25E9%2596%2580&datepicker=' 
        self.CSV_URL = url+self.date
        

    def run(self):
        
        r = requests.get(url=self.CSV_URL,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/537.36"

        })


        with open('text'+self.date+'.txt','w',encoding='utf-8') as w:
            w.write(r.text)
        #print('hi')
        arr(self.date)
        arr.Output(self)
        
