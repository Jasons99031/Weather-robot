import json



def text():
    data = {
    
    }

    data['A']='1'
    data['B']=[]#新增一個陣列
    data['B'].insert(0,'2')
    data['B'].insert(1,'3')



    with open('try.json','w') as fill:
        json.dump(data,fill)

    with open('try.json','r') as fill:
        data=json.load(fill)

    print(data)

text()

