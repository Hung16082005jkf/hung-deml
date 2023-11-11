yeu_cau = input("nếu sử dụng thư viện nhập có \nsử dụng thêm hàm nhập không: ")
tai_lieu = {"int()": "int() là hàm dùng để ép kiểu số nguyên \n cách sử dụng:int(obj)", 
            "float()": "float() là hàm dùng để ép kiểu số thực \n cách sử dụng:float(obj)", 
            "upper()": "upper() là hàm dùng để chuyển tất cả các ký tự trong sring sang dạng chữ hoa \n cách sử dụng:ten_tien.upper() ", 
            "lower()": "lower() là hàm dùng để chuyển tất cả các ký tự trong string sang dạng chữ thường \n cách sử dụng:ten_bien.lower()", 
            "pop()": "pop() là hàm dùng để xóa một phần tử trong string hoặc list bằng chỉ mục index \n cách sử dụng: ten_ham.pop([index])" }
if yeu_cau == "có":
    print(tai_lieu[input("nhập vào key_value:")])
if yeu_cau == "không":
    pass

them_vao = input("bạn muốn thêm hàm vào có/không: ")

if them_vao == "có":
     tai_lieu[input("Mời Nhập vào key value: ")] = input("Nhập vào định nghĩa: ")
if them_vao == "không":
    pass
   
print(tai_lieu)




