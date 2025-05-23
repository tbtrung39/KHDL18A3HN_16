a = int(input("Nhập tử số: "))
b = int(input("Nhập mẫu số: "))
while b == 0:
    print("Mẫu số không thể bằng 0! Vui lòng nhập lại.")
    b = int(input("Nhập mẫu số: "))
print(f"Phân số bạn nhập là: {a}/{b}")