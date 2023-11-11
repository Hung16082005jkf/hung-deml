so_luong_sinh_vien=int(input("Nhập vào số sinh viên: "))
danh_sach_sinh_vien=[]
tong_chieu_cao=0
so_luong_sinh_vien_co_chieu_cao_tren_TB=0
for i in range(1,so_luong_sinh_vien+1):
    chieu_cao=float(input("Nhập vào chiều cao của bạn thứ" + " " + str(i) +  ":"))
    tong_chieu_cao+=chieu_cao
    danh_sach_sinh_vien.append(chieu_cao)
print("chiều cao của các sinh viên là:",danh_sach_sinh_vien)
sinh_vien_cao_nhat=max(danh_sach_sinh_vien)
sinh_vien_thap_nhat=min(danh_sach_sinh_vien)
print("sinh viên cao nhất lớp có chiều cao là: ",sinh_vien_cao_nhat)
print("sinh viên thấp nhất lớp có chiều cao là: ",sinh_vien_thap_nhat)        
chieu_cao_trung_binh=tong_chieu_cao/so_luong_sinh_vien
print("chiều cao trung bình của cả lớp là: ",chieu_cao_trung_binh)
for i in range(so_luong_sinh_vien):
    if danh_sach_sinh_vien[i] >= chieu_cao_trung_binh:
        so_luong_sinh_vien_co_chieu_cao_tren_TB+=1
print("số lượng sinh viên có chiều cao trên trung bình là:",so_luong_sinh_vien_co_chieu_cao_tren_TB)
