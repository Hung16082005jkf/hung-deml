
n = int(input("Nhập vào số lượng dãy số: "))
tích = 1
so_le = []
for i in range(1,n+1):
    số = int(input("Nhập vào số thứ " + str(i) + ":"))
    if số<10:
        if số%2==0:
            tích = tích*số
        if số%2!=0:
            so_le.append(số)
    if số>10:
        if số%2!=0:
            so_le.append(số)        
if tích != 1:
    print(tích)
if tích == 1:
    print(max(so_le))
   
    
       





