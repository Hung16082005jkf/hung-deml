do_dai_cung_duong=[]
doan_duong=[]
van_toc=[]
thoi_gian_den_diem_bus=[]
so_luong_diem_bus=int(input("Nhập vào số lượng điểm bus: "))
su_dung=int(input("Nhập vào 1 or 0 or -1 : "))
lis=[[],[]]
ten=["van_toc","do_dai_cung_duong"]
def nhap_thong_tin(a,b,d,e):
    for i in range(1,a+b):
        c=input("Nhập vào" + d + "thứ" + str(i) + ":")
        e.append(c)
    return e
print(nhap_thong_tin(so_luong_diem_bus,su_dung,ten[0],lis[0]))
print(nhap_thong_tin(so_luong_diem_bus,su_dung,ten[1],lis[1]))
su_dung_1=int(input("Nhập vào 1 or 0 or -1 : "))
d=input("ký tự")
def tinh_toan(g,h,k):
    for i in range(1,g+h):
        j=int(lis[0][i-1]) + d + int(lis[1][i-1])
        k.append(j)
    return k
print(tinh_toan(so_luong_diem_bus,su_dung_1,thoi_gian_den_diem_bus))
print(thoi_gian_den_diem_bus)
