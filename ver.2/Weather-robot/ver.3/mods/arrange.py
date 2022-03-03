
from bs4 import BeautifulSoup
import json
import os
import time




class arr():
    
    def __init__(self,dete):
        
        self.date=dete
        

    def Output(self):

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
        

        with open('json_data\\'+self.date+'.txt','w',encoding='utf-8' ) as x:
            x.write(data)

            

        os.remove('raw_data\\text' + self.date + '.txt')
