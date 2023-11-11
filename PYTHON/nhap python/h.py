diem_tieu_chi=100
print("Tiêu chí cần có")
tieu_chi=["cân nặng (0)","chiều cao (1)","năm kinh ngiệm (2)","tuổi (3)","giới tính (4)"]
print(tieu_chi)
print("CHÚ THÍCH:\nNAM ĐIỀN 1\nNỮ ĐIỀN 0\nGIỚI TÍNH KHÁC ĐIỀN 3\n các giá trị (0),(1),(2),..là các id của tiểu chí")
a={0:" "}
for i in range(5):
   a[i]=int(input("nhập vào tiêu chí " + tieu_chi[i] + " "))

if 30<a[3]>40:
   if a[2] == 2:
      if 