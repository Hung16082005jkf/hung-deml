print("TRƯƠNG TRÌNH BUS MAP server")
do_dai_cung_duong=[]
doan_duong=[]
van_toc=[]
thoi_gian_den_diem_bus=[]
gio=[]
phut_1=[]
gio_xe_chay=float(input("CHÚ Ý:GHI GIỜ THEO CÚ PHÁp \nVD:1H30PHUT=1,3GIO \nNhập vào giờ xe chạy: "))
so_luong_diem_bus=int(input("Nhập vào số lượng điểm bus: "))
for i in range(1,so_luong_diem_bus+1):
    vi_tri=input("Nhập vào vị trí thứ" + " " + str(i) + ":")
    doan_duong.append(vi_tri)
for i in range(1,so_luong_diem_bus):
    khoang_cach=float(input("Nhập vào khoảng cách thứ" + str(i) + ":"))
    do_dai_cung_duong.append(khoang_cach)
for i in range(1,so_luong_diem_bus):
    toc_do_bus=float(input("Nhập vào vận tốc bus ở cung" + str(i) + ":"))
    van_toc.append(toc_do_bus)
for i in range(1,so_luong_diem_bus):
    thoi_gian=do_dai_cung_duong[0]/van_toc[0]
    thoi_gian_den_diem_bus.append(float(thoi_gian))
for i in range(so_luong_diem_bus-1):
    gio_xe_chay=gio_xe_chay+thoi_gian_den_diem_bus[i]
    h=int(gio_xe_chay)
    phut=(gio_xe_chay-h)*60
    gio.append(h)
    phut_1.append(phut)
print("TRƯƠNG TRINH BUS MAP CỦA NGƯỜI DÙNG")
vitri=input("nhập vào vị trí hiện tại của bạn: ")
diem_den=input("nhập vào điểm bạn muốn đến: ")
chi_muc=doan_duong.index(diem_den)
chi_muc_1=doan_duong.index(vitri)

print("thời gian xe đến nơi là %d giờ %d phút" %(gio[chi_muc_1-1],phut_1[chi_muc_1-1]))
print("thời gian đi đến điểm bạn tìm là %d giờ %d phút" %(gio[chi_muc-1],phut_1[chi_muc-1]))



