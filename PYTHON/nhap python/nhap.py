import math


while True:

	

	print("TRương trình kiểm tra và tính toán tam giác")

	canh_1 = float(input("Mời bạn nhập vào cạnh thứ nhất: "))
	canh_2 = float(input("Mời bạn nhập vào cạnh thứ hai: "))
	canh_3 = float(input("Mời bạn nhập vào cạnh thứ ba: "))

	if canh_1 > 0 and canh_2 > 0 and canh_3 > 0:
		print("THõa mãn là một tam giác")
		if canh_1 ** 2 == canh_2 ** 2 + canh_3 ** 2 or canh_2 ** 2 == canh_1 ** 2 + canh_3 ** 2 or canh_3 ** 2 == canh_1 ** 2 + canh_2 ** 2:
			print("Là tam giác vuông")
			if canh_1 ** 2 == canh_2 ** 2 + canh_3 ** 2:
				dien_tich = (canh_2 * canh_3) / 2
			if canh_2 ** 2 == canh_1 ** 2 + canh_3 ** 2:
				dien_tich = (canh_2 * canh_1) / 2
			if canh_3 ** 2 == canh_1 ** 2 + canh_2 ** 2:
				dien_tich = (canh_1 * canh_2) / 2
			print("Diện tích tam giác là%s" %(dien_tich))  
		if canh_1 == canh_2 == canh_3:
			print("Là tam giác đều")
			dien_tich = (canh_2 ** 2 * math.sqrt(3)) / 4
			print("Diện tích tam giác là%s" %(dien_tich))
		if canh_1 == canh_2 != canh_3 or canh_2 == canh_3 != canh_1 or canh_3 == canh_1 != canh_2:
			print("là tam giác cân")
			if canh_1 == canh_2 != canh_3:
				c =  math.sqrt(canh_1 ** 2 - (canh_3 / 2) ** 2)
				dien_tich = (canh_3 * c ) / 2
			if canh_2 == canh_3 != canh_1:
				c = math.sqrt(canh_2 ** 2 - (canh_1 / 2) ** 2)
				dien_tich = (canh_1 * c ) / 2
			if canh_3 == canh_1 != canh_2:
				c = math.sqrt(canh_3 ** 2 - (canh_2 / 2) ** 2)
				dien_tich = (canh_2 * c) / 2
			print("Diện tích tam giác là%s" %(dien_tich)) 
	if canh_1 <= 0 or canh_2 <= 0 or canh_3 <= 0:
		print("Không phải là tam giác")
	if canh_1 == canh_2 == canh_3 == 13:
		break




