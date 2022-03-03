

from mod.data_date import date_req

A=date_req(2021,1,1,2021,12,31)#下載資料

A.loop()

from mod.data_r import date_read

B=date_read(2021,1,1,2021,12,31) #可以抓出哪些天有起霧

B.loop()
#