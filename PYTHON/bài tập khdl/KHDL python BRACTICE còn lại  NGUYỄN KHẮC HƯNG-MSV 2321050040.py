tong=0
danh_sach_so_nguoi_dung_da_nhap=[]
so_nguoi_dung_nhap_vao=int(input("Nhập vào số lượng số bạn muốn nhập: "))
for i in range(1,so_nguoi_dung_nhap_vao+1):
    nguoi_dung_nhap=int(input("Nhập vào số thứ " + str(i) + ":"))
    tong+=nguoi_dung_nhap
    danh_sach_so_nguoi_dung_da_nhap.append(nguoi_dung_nhap)
print("danh sách người dùng nhập là: ",danh_sach_so_nguoi_dung_da_nhap)
print("Tông các số mà người dùng nhập vào là:",tong)