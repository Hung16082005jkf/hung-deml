print("MÁY BÁN NƯỚC CÔNG NGHỆ CAO")
do_uong={"coca":35000, "nước cam":40000, "trà sữa":50000,
         "nước dừa":100000, "nước xấu":500000, "nước mơ":1000000,
         "nước tranh":34000, "nước mưa":50000, "nước khoáng":100000}
print(do_uong)
khach_hang=input("mời bạn chọn đồ uống: ")
so_luong=int(input("mời bạn nhập số lượng muốn mua: "))
thanh_tien=do_uong[khach_hang]*so_luong
print("Số tiền bạn phải trả là:%d"%(thanh_tien))