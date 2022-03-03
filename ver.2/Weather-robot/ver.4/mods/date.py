import os


class date_Record():#產生從一個日期到另一個日期中間的所有日期的文檔
    
    def __init__(self,Ny,Nm,Nd,My,Mm,Md):

        try:
            os.remove("day.txt")

            with open('day.txt','w',encoding='utf-8') as w:
                w.write("")        
        except:
            with open('day.txt','w',encoding='utf-8') as w:
                w.write("")

        self.My = My
        self.Mm = Mm
        self.Md = Md
        self.Ny = Ny
        self.Nm = Nm
        self.Nd = Nd
        
        self.output = ''
        self.Day = ''

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
                #print('Y')#看到對的Y了嗎            


            while self.Nm<=12 and M:  
                

                if self.Nm<10:
                    sm = '0'+str(self.Nm)
                else:
                    sm = str(self.Nm) 



                if not(Y) and self.Mm==self.Nm:
                    M=0
                    #print('M')#看到對的M了嗎

                
                
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

                        self.output = str(self.Ny)+'-'+str(sm)+'-'+str(sd) #輸出的格式
                    

                        #print('D')看到對的D了嗎
                    else:
                        D=1  

                        
                        if self.Nd<10:
                            sd = '0'+str(self.Nd)
                        else:
                            sd = str(self.Nd)

                        self.output = str(self.Ny)+'-'+str(sm)+'-'+str(sd) #輸出的格式
                        


                        i+=1

                        
                        
                        self.Nd+=1

                    if(i-1):
                        self.Day=self.Day+","+self.output#把資料串在一起
                    else:
                        self.Day=self.output
                        
                


                M=1
                self.Nd=1
                self.Nm+=1

                #print('m') #分割月份?   
                    


            if self.My!=self.Ny:
                Y=1
                self.Nm=1 
                self.Ny+=1                    
                    
                print(self.Ny)
            with open('day.txt','r',encoding='utf-8') as r:
                R=r.read()
                with open('day.txt','w',encoding='utf-8') as w:
                    w.write(R+self.Day)
            self.Day=''
            


                                
                                
        
        



                    
        




            

    