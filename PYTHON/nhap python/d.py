import requests
import json
a = input("Nhập vào đường link: ")
req=requests.get('https://humg-khdl-k68.nguyen-ngocng72.repl.co/demo/json/my.php?url=' + a)
ket_qua=req.json()['result_url']
print(ket_qua)


