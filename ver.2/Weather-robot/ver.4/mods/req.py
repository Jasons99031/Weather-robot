import requests
import threading



class Req(threading.Thread):
    def __init__(self,dete): 
        threading.Thread.__init__(self) #要用threading funtion 要叫run
        self.date=dete
        url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467110&stname=%25E9%2587%2591%25E9%2596%2580&datepicker=' 
        self.CSV_URL = url+self.date#金門某年某月某日

    def date_read(self):

        threads = [] #並排運算的陣列

        with open('input.txt','r',encoding='utf-8') as r:#讀取date所產生的txt
            R=r.read()                                       #
            P=R.split(',')                                   #用，篩選
        for i in range(0,len(P)):
            date=P[i]
            #print(date+'=')
            threads.append(Req(date))#將日期傳給Req抓檔案
            threads[i].start()#讓Req開始

        


    def run(self):
        
        r = requests.get(url=self.CSV_URL,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/537.36"

        })


        with open('raw_data\\text'+self.date+'.txt','w',encoding='utf-8') as w:
            w.write(r.text)
            #print(self.date +'__') 
