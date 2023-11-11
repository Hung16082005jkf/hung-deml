print("TRƯƠNG TRÌNH TÍNH TIỀN SIÊU THỊ")
gia_mat_hang={"táo":14000,"dưa hấu":20000,"sữa":10000,
              "thịt":100000,"kiwi":70,"bơ":120000,
              "thịt bò":200000,"bánh chocobyt":70000,
              "rau chân vịt":10000}
print("chú ý: \nthit là tính trên cân \nrau là tính trên bó \nsữa bánh là tính trên sản phẩm")
mat_hang_khạch_mua=input("Nhập vào hàng khách mua: ")
so_luong=float(input("nhập vào số lượng khách mua: "))
tien_khach=int(input("Nhập vào tiền khách đưa: "))
tien_phai_tra=gia_mat_hang[mat_hang_khạch_mua]*so_luong
if tien_phai_tra<tien_khach:
    print("khách đã đưa thừa")
    tien_thoi = tien_khach - tien_phai_tra
    print(tien_thoi)
    if tien_thoi<50000:
        if tien_thoi%10000==0:
            tra_lai=tien_thoi//10000
            print("cần trả lại khách %d tờ 10000" %(tra_lai))
        if tien_thoi%10000!=0:
            du=tien_thoi%10000
            tra_lai=tien_thoi//10000
            print("cần phải trả cho khách %d tờ 10000 và %d " %(tra_lai,du))
    if 50000<tien_thoi<100000:
        tra_lai=(tien_thoi-50000)//10000
        du=(tien_thoi-50000)%10000
        print("phải trả cho khách 1 tờ 50000 và %d tờ 10000 và %d" %(tra_lai,du))
elif tien_phai_tra>tien_khach:
    print("khách đã thiếu")
    tien_thieu = tien_phai_tra - tien_khach
    print(tien_thieu)
    if tien_thieu<50000:
        if tien_thieu%10000==0:
            tra_lai=tien_thieu//10000
            print("cần thêm  %d tờ 10000" %(tra_lai))
        if tien_thieu%10000!=0:
            du=tien_thieu%10000
            tra_lai=tien_thieu//10000
            print("cần thêm %d tờ 10000 và %d " %(tra_lai,du))
    if 50000<tien_thieu<100000:
        tra_lai=(tien_thieu-50000)//10000
        du=(tien_thieu-50000)%10000
        print("cần thêm 1 tờ 50000 và %d tờ 10000 và %d" %(tra_lai,du))
else:
    print("khách đã đưa đủ ")
