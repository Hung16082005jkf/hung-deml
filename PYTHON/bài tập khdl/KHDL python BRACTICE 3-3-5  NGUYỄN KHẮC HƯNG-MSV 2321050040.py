import datetime
from datetime import date, datetime
print("TRƯƠNG TRÌNH CHAT POT ")
while True:
    yeu_cau=input("Nhập vào yêu cầu của bạn: ")
    if "chủ tịch nước" in yeu_cau:
        computer="Nguyễn Xuân Phúc"
    elif "ngày bao nhiêu" in yeu_cau:
        today = date.today()
        computer = today.strftime("%B %D, %Y")
    elif "mấy giờ" in yeu_cau:
        now = datetime.now()
        computer = now.strftime("%H hours %M minutes %S seconds")
    elif "CEO GG" in yeu_cau:
        computer="Sundar Pichai"
    elif "CEO FB" in yeu_cau:
        computer="Mark Elliot Zuckerberg"
    elif "giàu nhất việt nam" in yeu_cau:
        computer="Phạm Nhật Vượng"
    elif "Giàu nhất thế giới" in yeu_cau:
        computer="elon murk"
    elif "chủ tịch fpt" in yeu_cau:
        computer="Hoàng Nam Tiến"
    elif "chủ tịch sunhose" in yeu_cau:
        computer="Shark phú"
    elif "data scient" in yeu_cau:
        computer="""Khoa học dữ liệu (KHDL) là 
        khoa học về việc quản trị và phân tích
        dữ liệu để tìm ra các hiểu biết, các tri thức hành động, 
        các quyết định dẫn dắt hành động. KHDL gồm ba phần chính:
        Tạo ra và quản trị dữ liệu, phân tích dữ liệu, và chuyển kết quả phân tích thành giá trị của hành động.
        Nôm na bước thứ nhất là về số hóa và bước thứ hai là về dùng dữ liệu.
        Việc phân tích và dùng dữ liệu lại dựa vào ba nguồn tri thức: 
        toán học (thống kê toán học), công nghệ thông tin (máy học) và tri thức của lĩnh vực ứng dụng cụ thể"""
    elif "tạm biệt" in yeu_cau:
        computer="Tạm biệt bạn"
        print(computer)
        break
    else:
        computer="Tôi chưa được biết thông tin này"
    print("theo tôi câu trả lời là " + computer)
 