ten_nguoi_dung=str(input("Nhập vào tên của bạn: "))
print("xin chào " + ten_nguoi_dung)
yeu_cau=int(input("bạn muốn mua bao nhiêu ly trà sữa trân trâu đen: "))
gia_1_ly_tran_chau_den=35000
thanh_tien=gia_1_ly_tran_chau_den*yeu_cau
print("Hóa đơn của bạn là\n%d nhân với 35k bằng %d\ntổng thanh toán của bạn là %d"%(yeu_cau,thanh_tien,thanh_tien))