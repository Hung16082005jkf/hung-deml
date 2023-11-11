import requests
import json

out = open('data-hs.txt', 'w')

ogSBD = 1077549

kq = []
for i in range(10):
    newSBD = str('0' + str(ogSBD))
    #print(newSBD)
    
    a = requests.get(f'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords={newSBD}')
    kq.append({
        str(a.json()[0]["SOBAODANH"]): a.json()[0]["TOAN"]
    })

    ogSBD += 1

print(kq)
#out.write(json.dumps(kq))

out.write('dcmm')


