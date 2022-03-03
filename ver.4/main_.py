
from mods.date import date_Record
from mods.req import Req
from mods.arrange2json import arr
import os




def Download_data(y,m,d,Y,M,D):#這邊有很大一部份是在確認之前有無下載過，減少重複下再浪廢資源
    record = []                    #os有查看是否有這個檔案isfile()
    record_w = ""
    try:
        with open('h_r.txt','r',encoding='utf-8') as r:

            record_w= r.read()                                       
            P = record_w.split(',')
            record = P

            print(len(P))
    except:
        with open('h_r.txt','w',encoding='utf-8') as r:
            pass
        os.mkdir("raw_data")
        os.mkdir("json_data")


    print(y,m,d,Y,M,D)
    First=date_Record(y,m,d,Y,M,D)#下載範圍
    First.loop()#產生所需日期的數列(txt)

 
        
    with open('day.txt','r',encoding='utf-8') as r:#讀取date所產生的txt
            R=r.read()                                       
            P=R.split(',')

            

            needReq = ""
            for i in range(0,len(P)):
                date=P[i]
                try:
                    record.index(date)
                    
                except:
                    if(record_w!=""):
                        record_w= record_w+',' + date
                        print(date)
                    else:
                        record_w = date
                    if (needReq!=""):
                        needReq = needReq+',' +date
                    else:
                        needReq = date
    with open("h_r.txt",'w',encoding='utf-8') as w:

            w.write(record_w)
    with open("input.txt",'w',encoding='utf-8') as w:

            w.write(needReq)



    Second = Req.date_read("")#啟動下載
    Second
    
    third = arr.date_read("")#啟動整理
    third





y=2015
m=1
d=1
Y=2021
M=12
D=31

Q = input("是否下載"+str(y)+'_'+str(m)+'_'+str(d)+'到'+str(Y)+'_'+str(M)+'_'+str(D)+' 1 or 0 ?\n')
if Q=='1':
    Download_data(y,m,d,Y,M,D)
else:    
    R = input('輸入起始和終點')
    P=R.split(' ')
    print(int(P[1]))
    Download_data(int(P[0]),int(P[1]),int(P[2]),int(P[3]),int(P[4]),int(P[5]))
