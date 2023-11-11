yeu_cau=input("Bạn muốn sử dụng trương trình nào: ")

#-HW 11
if "bia" in yeu_cau:
    print("TRƯƠNG TRÌNH TÍNH TIỀN BIA")
    so_bia=int(input("Nhập vào số chai bia mà bạn mua: "))
    gia=int(input("Nhập vào giá tiền bạn mua bia: "))
    thanh_tien=so_bia*gia
    print("Số tiền bạn phải trả là %d"%(thanh_tien))

#-HW 12
if "tuổi" in yeu_cau: 
    print("TRƯƠNG TRÌNH TÍNH TUỔI")
    nam_sinh_cua_ban=int(input("Nhập vào năm sinh của bạn: "))
    nam_hien_tai=2023
    tuoi_cua_ban=nam_hien_tai-nam_sinh_cua_ban
    print("Tuổi của bạn là %d"%(tuoi_cua_ban))

#-HW 13
if "tam giác" in yeu_cau:
    print("TRƯƠNG TRÌNH TÍNH CHU VI TAM GIÁC")
    chu_vi_tam_giac_la=0
    for i in range(1,4):
        canh=int(input("Nhập vào chiều dài cạnh thứ " + str(i) + ":"))
        chu_vi_tam_giac_la+=canh
    print("Chu vi của tam giác là:%d"%(chu_vi_tam_giac_la))
#-HW 14
if "cổ phiếu" in yeu_cau:
    print("TRƯƠNG TRÌNH TÍNH TIỀN CỔ PHIẾU")
    so_co_phieu=int(input("Nhập số cổ phiếu bạn mua: "))
    gia_co_phieu=int(input("Nhập vào giá cổ phiếu bạn mua: "))
    tong_tien_co_phieu=so_co_phieu*gia_co_phieu
    print("số tiền bạn phải trả là:%d"%(tong_tien_co_phieu))
