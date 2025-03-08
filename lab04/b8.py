num = input("Nhập một số nguyên: ")
num = num.lstrip('-')
tong = sum(int(ch) for ch in num)
print("Tổng các chữ số của số đã nhập là:", tong)
