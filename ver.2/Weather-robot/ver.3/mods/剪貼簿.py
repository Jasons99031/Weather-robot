try:
    os.remove("input_day.txt")

    with open('input_day.txt','w',encoding='utf-8') as w:
        w.write("")        
except:
    with open('input_day.txt','w',encoding='utf-8') as w:
        w.write("")




with open('input_day.txt','r',encoding='utf-8') as r:
    R=r.read()
    with open('input_day.txt','w',encoding='utf-8') as w:
        w.write(R+','+self.output)


while 1:
    try:
        with open('raw_data\\text' + self.date + '.txt','r',encoding='utf-8') as a:
            html = a.read()
            arr = BeautifulSoup(html,'html.parser')
            t = arr.find_all('th')
            q = arr.find_all('td')
        break   
    except:
        time.sleep(5)