import requests
req=requests.get('https://vietnamnet.vn/giao-duc/diem-thi/tra-cuu-diem-thi-tot-nghiep-thpt/2023/01086796.html')
son=open("kiw.txt", "w",encoding="UTF-8")
son.close()
son.write(str(req.text))

