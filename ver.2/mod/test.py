import json

with open('test.txt','r',encoding='utf-8') as F:
    D=dict(json.load(F))
    print(D["A"][2]["ObsTime"][1])

