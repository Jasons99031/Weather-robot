def all_data(yN,mN,dN,yM,mM,dM):
    

    Y=1
    M=1
    D=1

    while Y:
        
        
        if yM==yN:
            Y=0
            print('Y')
        else:
            Y=1
            mN=1
            yN+=1

        while mN<12 and M:

                
            if not(Y) and mM==mN:
                M=0
                print('M')
            else:
                M=1
                dN=1
                mN+=1

            
            
            if (mN<8 and mN%2) or (mN>7 and not(mN%2)):
                Day=31
            else:
                if mN!=2:
                    Day=30
                else:
                    if ( not(yN%4) and (yN%100)) or not(yN%400) :

                        Day=29
                    else:
                        Day=28
            while dN<Day and D:

                if not(M) and dM+1==dN:
                    D=0
                    print('D')
                else:
                    D=1  

                    if mN<10:
                        sm = '0'+str(mN)
                    else:
                        sm = str(mN) 
                    if dN<10:
                        sd = '0'+str(dN)
                    else:
                        sd = str(dN)

                    data = str(yN)+'-'+str(sm)+'-'+str(sd)
                    print(data)
                    #Req(data)
                    #arrange(data)

                    dN+=1
                

                
                
            #print(data)
                


        



yN=2020
mN=1
dN=10

yM=2020
mM=1
dM=20



all_data(yN,mN,dN,yM,mM,dM)











'''
                                    #mod=0,1,2,3
                                     # (0) 單存輸出時間      
                                     # (1) 請求檔案 and (0)
                                     # (2) 整合資料 and (0)
                                     # (3) (1) and (2)
                print(data)
                if mod==1 or mod==3:
                    Req(data)
                    arrange(data)
                if mod==2 or mod==3:
                    
                    fusion(file_name,data)
'''

