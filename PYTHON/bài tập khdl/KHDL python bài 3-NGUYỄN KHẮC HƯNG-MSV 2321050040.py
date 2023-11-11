n = int(input("Nhập vào số lượng hàng: "))
ten_hang = {}
so_luong = 0
for i in range(1,n+1):
    suat_su = input("Nhập vào suất sứ: ")
    ten_hang[input("Nhập vào tên hàng:")] = suat_su
    if "việt nam" in suat_su:
        so_luong = so_luong + 1
print(ten_hang)
print(so_luong)