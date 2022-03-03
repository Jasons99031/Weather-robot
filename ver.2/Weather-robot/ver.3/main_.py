from mods.date import date_Record
from mods.req import Req
from mods.arrange import arr

def Download_data(y,m,d,Y,M,D):
    print(y,m,d,Y,M,D)
    First=date_Record(y,m,d,Y,M,D)#下載範圍
    First.loop()

    Second = Req.date_read('')#啟動下載
    Second
    with open('input_day.txt','r',encoding='utf-8') as r:#將下載的HTML整理成JSON
        R=r.read()
        P=R.split(',')
    for i in range(1,len(P)):
        date=P[i]
        Third=arr(date)
        Third.Output()





y=2022
m=1
d=1
Y=2022
M=1
D=1

Q = input("是否下載"+str(y)+'_'+str(m)+'_'+str(d)+'到'+str(Y)+'_'+str(M)+'_'+str(D)+' 1 or 0 ?\n')
if Q=='1':
    Download_data(y,m,d,Y,M,D)
else:    
    R = input('輸入起始和終點')
    P=R.split(' ')
    print(int(P[1]))
    Download_data(int(P[0]),int(P[1]),int(P[2]),int(P[3]),int(P[4]),int(P[5]))
