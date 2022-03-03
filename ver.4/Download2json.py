################很有問題########
import threading
import requests
from bs4 import BeautifulSoup
import json
import os
import time

from mods.date import date_Record

class D2J( threading.Thread):

    def __init__(self,dete): 
        threading.Thread.__init__(self) #要用threading funtion 要叫run
     
        self.date=dete
        url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467110&stname=%25E9%2587%2591%25E9%2596%2580&datepicker=' 
        self.CSV_URL = url+self.date#金門某年某月某日




    def GO(self,y, m , d ,Y , M , D ):
        record = []
        record_w = ""
        try:
            with open('h_r.txt','r',encoding='utf-8') as r:

                record_w= r.read()                                       
                c = record_w.split(',')
                record = c

                #print(len(P))
        except:
            with open('h_r.txt','w',encoding='utf-8') as r:
                pass
            os.mkdir("raw_data")
            os.mkdir("json_data")
        
        threads = []

        day = date_Record(y,m,d,Y,M,D)
        day.loop()
        with open('input_day.txt','r',encoding='utf-8') as r:#讀取date所產生的txt
                R=r.read()                                       
                P=R.split(',')

                
                j = 0
                for i in range(0,len(P)):
                    date=P[i]
                    try:
                        record.index(date)
                        
                    except:
                        if(record_w!=""):
                            record_w= record_w+',' + date
                            
                        else:
                            record_w = date
                        threads.append(D2J(date))
                        threads[j].start()
                        j+=1
                
        with open("h_r.txt",'w',encoding='utf-8') as w:

                w.write(self.record_w)



    def run(self):
        self.req(self.date)
        self.arr2json(self.date)
    


    def req(self):
        
        r = requests.get(url=self.CSV_URL,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/537.36"

        })


        with open('raw_data\\text'+self.date+'.txt','w',encoding='utf-8') as w:
            w.write(r.text)
            #print(self.date +'__') 



    def arr2json(self):

        while 1:#因為並列下載是並列執行有可能還沒載好前面的，需要先等待
            try:
                with open('raw_data\\text' + self.date + '.txt','r',encoding='utf-8') as a:
                    html = a.read()
                    arr = BeautifulSoup(html,'html.parser')
                    t = arr.find_all('th')
                    q = arr.find_all('td')
                break   
            except:
                print('wait')
                time.sleep(0.1)

        R=0
        i=0
        File=dict()
        keys=[]
        for key in t:
            
            K=key.string
            

            if  K=='ObsTime':
                R=1
            

            if R:
                
                
                keys.append(K)
                f=dict([[K,[]]])
                File.update(f)
                
        #print(File)





        R=0
        i=0

        #print(keys)

        for v in q:
            if v.string == '01':#找資料的開頭
                R=1
            if R:




                try:    #將資料轉成數字
                    T = float(v.string)
                except ValueError:
                    T = str(v.string)
                    T=T.strip('\xa0')
                File[keys[i]].append(T)


                #print(v.string)
                i+=1
            if i>16:
                i=0

        
        data = json.dumps(File)
        

        with open('json_data\\'+self.date+'.json','w',encoding='utf-8' ) as x:
            x.write(data)

        while 1:    
            try:
                os.remove('raw_data\\text' + self.date + '.txt')
                break 
            except:
                time.sleep(0.1)
y=2015
m=3
d=3
Y=2015
M=4
D=4

A=D2J("")

Q = input("是否下載"+str(y)+'_'+str(m)+'_'+str(d)+'到'+str(Y)+'_'+str(M)+'_'+str(D)+' 1 or 0 ?\n')
if Q=='1':
    A.GO(y,m,d,Y,M,D)
    
else:    
    R = input('輸入起始和終點')
    P=R.split(' ')
    print(int(P[1]))
    A.GO(int(P[0]),int(P[1]),int(P[2]),int(P[3]),int(P[4]),int(P[5]))


