from .read_ import Read_
import threading

class date_read(threading.Thread):
    
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



        Y=1
        M=1
        D=1
        i=0

        while Y:
            
            if self.My==self.Ny:
                Y=0
                print('Y')            


            while self.Nm<=12 and M:  
                

                if self.Nm<10:
                    sm = '0'+str(self.Nm)
                else:
                    sm = str(self.Nm) 



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

 
                        if self.Nd<10:
                            sd = '0'+str(self.Nd)
                        else:
                            sd = str(self.Nd)

                        self.output = str(self.Ny)+'-'+str(sm)+'-'+str(sd)
                        filename = str(self.Ny)+'-'+str(sm)
                        R=Read_(self.output,filename,self.Ny)
                        #R.read_D_TO_M() #將風向統計並將整合成每月一筆
                        R.read_fog()#統計霧
                        
                        #print(i)
                        #print(self.output)

                        print('D')
                    else:
                        D=1  

                        
                        if self.Nd<10:
                            sd = '0'+str(self.Nd)
                        else:
                            sd = str(self.Nd)

                        self.output = str(self.Ny)+'-'+str(sm)+'-'+str(sd)
                        filename = str(self.Ny)+'-'+str(sm)

                        R=Read_(self.output,filename,self.Ny)
                        #R.read_D_TO_M()#將風向統計並將整合成每月一筆
                        R.read_fog()#統計霧


                        #print(i)
                        #print(self.output)

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




                    
        




            

    