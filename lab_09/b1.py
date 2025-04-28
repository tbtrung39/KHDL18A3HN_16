def find_max(a, b, c):
    # So sánh 2 số a và b trước
    if a > b:
        max_ab = a
    else:
        max_ab = b
    
    # So sánh max_ab với c
    if max_ab > c:
        return max_ab
    else:
        return c

# Nhập 3 số từ bàn phím
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ ba: "))

# Gọi hàm tìm max
result = find_max(x, y, z)
print("Số lớn nhất là:", result)
