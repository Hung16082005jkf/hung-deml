if tong_diem>=22:
    thi_sinh="CNTT,CNTT CHẤT LƯỢNG CAO,ĐỊA CHẤT,KHDL,MÔI TRƯỜNG"
if 18<=tong_diem<22:
    thi_sinh="CNTT,KHDL,ĐỊA CHẤT,MÔI TRƯỜNG"
if 17<=tong_diem<18:
    thi_sinh="địa chất, môi trường"
if 15<=tong_diem<17:
    thi_sinh="địa chất"
if tong_diem<15:
    thi_sinh="Không đỗ nghành nào"
print("thí sinh đã đỗ các nghành sau:", thi_sinh)