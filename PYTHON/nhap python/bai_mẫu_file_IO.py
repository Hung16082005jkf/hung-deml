user_number=int(input("Nhập vào một số bất kì: "))
with open("nth","w",encoding="UTF-8") as file:
    for i in range(user_number):
        a=user_number-i
        file.write(str(a) + "\n")
with open("nth","r",encoding="UTF-8") as file:
    data=file.read().split("\n")
    data.pop()
for i in range(1,len(data)+1):
    print("line " + str(i) + ": " + data[i-1])