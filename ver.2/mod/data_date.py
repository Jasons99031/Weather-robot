
from .req import Req
import threading

class date_req(threading.Thread):
    
    def __init__(self,Ny,Nm,Nd,My,Mm,Md):
        
        self.My = My
        self.Mm = Mm
        self.Md = Md
        self.Ny = Ny
        self.Nm = Nm
        self.Nd = Nd
        
        self.output = ''
    
    def test(self):
        print('A')

    def loop(self): 

        threads = [] #並排運算的陣列

        Y=1
        M=1
        D=1
        i=0

        while Y:
            
            if self.My==self.Ny:
                Y=0
                print('Y')            


            while self.Nm<=12 and M:

                    
                if not(Y) and self.Mm==self.Nm:
                    M=0
                    print('M')

                
                
                if (self.Nm<8 and self.Nm%2) or (self.Nm>7 and not(self.Nm%2)): #大小月
                    Day=31
                else:
                    if self.Nm!=2:
                        Day=30
                    else:
                        if ( not(self.Ny%4) and (self.Ny%100)) or not(self.Ny%400) : #閏年

                            Day=29
                        else:
                            Day=28


                while self.Nd<=Day and D:

                    if not(M) and self.Md==self.Nd:
                        D=0

                        if self.Nm<10:
                            sm = '0'+str(self.Nm)
                        else:
                            sm = str(self.Nm) 
                        if self.Nd<10:
                            sd = '0'+str(self.Nd)
                        else:
                            sd = str(self.Nd)

                        self.output = str(self.Ny)+'-'+str(sm)+'-'+str(sd)
                        
                        threads.append(Req(self.output))
                        

                        threads[i].start()
                        
                        #print(i)
                        print(self.output)

                        print('D')
                    else:
                        D=1  

                        if self.Nm<10:
                            sm = '0'+str(self.Nm)
                        else:
                            sm = str(self.Nm) 
                        if self.Nd<10:
                            sd = '0'+str(self.Nd)
                        else:
                            sd = str(self.Nd)

                        self.output = str(self.Ny)+'-'+str(sm)+'-'+str(sd)#變成網址需要的格式
                        
                        threads.append(Req(self.output))#將日期傳給Req抓檔案
                        

                        threads[i].start()#讓Req開始
                        
                        #print(i)
                        print(self.output)

                        i+=1

                        
                        
                        self.Nd+=1
                    #print('b')
                        
                
                



                M=1
                self.Nd=1
                self.Nm+=1
                print('m') #分割月份?   
                    


            if self.My!=self.Ny:
                Y=1
                self.Nm=1
                self.Ny+=1                    
                    
                #print(data)




                    
        




            

    