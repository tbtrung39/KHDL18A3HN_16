#Bài 4:
while True:
    tu_so = int(input("Nhập tử số: "))
    mau_so = int(input("Nhập mẫu số: "))
    if mau_so != 0:
        break
    print("Mẫu số không được bằng 0, vui lòng nhập lại!")

print(f"Phân số bạn đã nhập: {tu_so}/{mau_so}")