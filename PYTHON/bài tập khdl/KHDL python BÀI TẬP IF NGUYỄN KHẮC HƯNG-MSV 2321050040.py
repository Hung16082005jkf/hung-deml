
ten_mon_hoc=["toán","Lý","Hóa"]
tong_diem=0
for i in range(1,4):
    diem=float(input("Nhập vào điểm môn " + ten_mon_hoc[i-1] + ":"))
    tong_diem+=diem
b1=[22,18,17,15,0]
c1=[30,22,18,17,15]
thi_sinh=[["CNTT,CNTT CHẤT LƯỢNG CAO","ĐỊA CHẤT","KHDL","MÔI TRƯỜNG"],
          ["CNTT","ĐỊA CHẤT","KHDL","MÔI TRƯỜNG"],
          ["ĐỊA CHẤT","MÔI TRƯỜNG"],
          ["MÔI TRƯỜNG"],
          ["bạn đã trượt"]]
def hung(a,b,c):
    for i in range(5):
        if b[i]<=a<c[i]:
            nghanh_do=thi_sinh[i]
            return nghanh_do
print("các nghành bạn đã đỗ là:",hung(tong_diem,b1,c1))