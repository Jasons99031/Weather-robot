import threading
import requests

def Req(date):

    url='https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467110&stname=%25E9%2587%2591%25E9%2596%2580&datepicker=' 
    CSV_URL = url+date
    #print(CSV_URL)
    print(date + 'star')
    with requests.Session() as s: #下載HTML
        download = s.get(CSV_URL) 
        #print(download.text)
        content=download.text

    with open(date+".txt",'w') as f:#將資料存在筆記本
        f.write(content)
        print(date + 'OK')

'''
# 建立一個子執行緒
t = threading.Thread(target = "function")

# 執行該子執行緒
t.start()
'''
def test(num):        
    for i in range(40):
        i+=1
        print(i,num)

date=[
    '2005-01-01',
    '2005-01-02',
    '2005-01-03',
    '2005-01-04',
    '2005-01-05',
    '2005-01-06',
    '2005-01-07',
    '2005-01-08',
    '2005-01-09',
    '2005-01-10',
    '2005-01-11'
    ]

T=[]

for i in range(10):
    j=date[i]
    T.append(threading.Thread( target=Req ,args=(j,) ))
    T[i].start()