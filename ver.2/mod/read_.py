import json



class Read_():
    def __init__(self,date,filename,year):
        self.date=date
        self.filename=filename
        self.year=year
    
    def read_D_TO_M(self):

        try: 
            with open('.'+self.filename +'.txt','r',encoding='utf-8') as F:
                WD = dict(json.load(F))
                #print('OK')
            
        except:
            #print('NO')
            WD={
            '0.0':0,
            '10.0':0,
            '20.0':0,
            '30.0':0,
            '40.0':0,
            '50.0':0,
            '60.0':0,
            '70.0':0,
            '80.0':0,
            '90.0':0,
            '100.0':0,
            '110.0':0,
            '120.0':0,
            '130.0':0,
            '140.0':0,
            '150.0':0,
            '160.0':0,
            '170.0':0,
            '180.0':0,
            '190.0':0,
            '200.0':0,
            '210.0':0,
            '220.0':0,
            '230.0':0,
            '240.0':0,
            '250.0':0,
            '260.0':0,
            '270.0':0,
            '280.0':0,
            '290.0':0,
            '300.0':0,
            '310.0':0,
            '320.0':0,
            '330.0':0,
            '340.0':0,
            '350.0':0,
            '360.0':0,
            'V':0,
            'X':0
        }


        with open('./first/'+self.date+'.txt','r',encoding='utf-8') as F:

            D=dict(json.load(F))
            for i in D['WD']:
                WD[str(i)]+=1
            
        print(WD)

        with open('.'+self.filename+'.txt','w',encoding='utf-8') as F:
            File=json.dumps(WD)
            F.write(File)
    


    def read_fog(self):
        try: 
            with open('./fog/.Visb_'+str(self.year) +'.txt','r',encoding='utf-8') as F:
                Be_WD = dict(json.load(F))
                #print('OK')

            with open('./fog/.Visb_all'+str(self.year) +'.txt','r',encoding='utf-8') as F:
                WD = dict(json.load(F))
                #print('OK_all')

        except:
            Be_WD={
            '0.0':0,
            '10.0':0,
            '20.0':0,
            '30.0':0,
            '40.0':0,
            '50.0':0,
            '60.0':0,
            '70.0':0,
            '80.0':0,
            '90.0':0,
            '100.0':0,
            '110.0':0,
            '120.0':0,
            '130.0':0,
            '140.0':0,
            '150.0':0,
            '160.0':0,
            '170.0':0,
            '180.0':0,
            '190.0':0,
            '200.0':0,
            '210.0':0,
            '220.0':0,
            '230.0':0,
            '240.0':0,
            '250.0':0,
            '260.0':0,
            '270.0':0,
            '280.0':0,
            '290.0':0,
            '300.0':0,
            '310.0':0,
            '320.0':0,
            '330.0':0,
            '340.0':0,
            '350.0':0,
            '360.0':0,
            'V':0,
            'X':0
            }
            WD={
            '0.0':0,
            '10.0':0,
            '20.0':0,
            '30.0':0,
            '40.0':0,
            '50.0':0,
            '60.0':0,
            '70.0':0,
            '80.0':0,
            '90.0':0,
            '100.0':0,
            '110.0':0,
            '120.0':0,
            '130.0':0,
            '140.0':0,
            '150.0':0,
            '160.0':0,
            '170.0':0,
            '180.0':0,
            '190.0':0,
            '200.0':0,
            '210.0':0,
            '220.0':0,
            '230.0':0,
            '240.0':0,
            '250.0':0,
            '260.0':0,
            '270.0':0,
            '280.0':0,
            '290.0':0,
            '300.0':0,
            '310.0':0,
            '320.0':0,
            '330.0':0,
            '340.0':0,
            '350.0':0,
            '360.0':0,
            'V':0,
            'X':0
            }

        with open('./first/'+self.date+'.txt','r',encoding='utf-8') as F:

            D=dict(json.load(F))
            i=0
            
            while i<24:
                
                if D['Visb'][i]!="...":
                    try:
                        if D['RH'][i]>70 and D['Visb'][i]<=1:#判斷是否為霧
                            print(self.date +'fog')
                            i=25#跳脫
                            #Be_WD[str(D["WD"][i])] += 1#紀錄有起霧的

                        #WD[str(D["WD"][i])]+=1#紀錄有測Visb的
                    except:
                        i=i
                i+=1

        with open('./fog/.Visb_'+str(self.year)+'.txt','w',encoding='utf-8') as F:
            File=json.dumps(Be_WD)
            F.write(File) 
        with open('./fog/.Visb_all'+str(self.year)+'.txt','w',encoding='utf-8') as F:
            File=json.dumps(WD)
            F.write(File) 








'''
def read_M_to_Y(Myear,myear):
    
    


    while myear<=Myear:
        a=open('._.'+str(myear)+'_3~5'+'.txt','w',encoding='utf-8')
        a.close()
        y_WD={   
            '0.0':0,
            '10.0':0,
            '20.0':0,
            '30.0':0,
            '40.0':0,
            '50.0':0,
            '60.0':0,
            '70.0':0,
            '80.0':0,
            '90.0':0,
            '100.0':0,
            '110.0':0,
            '120.0':0,
            '130.0':0,
            '140.0':0,
            '150.0':0,
            '160.0':0,
            '170.0':0,
            '180.0':0,
            '190.0':0,
            '200.0':0,
            '210.0':0,
            '220.0':0,
            '230.0':0,
            '240.0':0,
            '250.0':0,
            '260.0':0,
            '270.0':0,
            '280.0':0,
            '290.0':0,
            '300.0':0,
            '310.0':0,
            '320.0':0,
            '330.0':0,
            '340.0':0,
            '350.0':0,
            '360.0':0,
            'V':0,#風向不定
            'X':0#故障
        }

        m=3
        

        while m<=5:
            
            if m<10:
                M='-'+'0'+str(m)
            else:
                M='-'+str(m)

            with open('.'+str(myear)+M+'.txt','r',encoding='utf-8') as F:
                print('.'+str(myear)+M)
                D=dict(json.load(F))
                
                i=0.0

                while i<=360.0:
                    
                    y_WD[str(i)] += D[str(i)]
                    
                    i+=10

            with open ('._.'+str(myear)+'_3~5'+'.txt','w',encoding='utf-8')as W:    
                File=json.dumps(y_WD)
                W.write(File)

            #print(y_WD)

            m+=1

        myear+=1
        




read_M_to_Y(2021,2005)


'''