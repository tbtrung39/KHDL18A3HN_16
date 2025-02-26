# Nhập số nguyên từ người dùng
so_nguyen = int(input("Nhập một số nguyên: "))

if so_nguyen < 100:
    print('0')
else:
    so_hang_tram=(so_nguyen // 100) % 10

# Lấy và in chữ số hàng trăm
print("Chữ số hàng trăm của",so_nguyen,"là:",so_hang_tram)