# Nhập vào một số nguyên
n = int(input("Nhập một số nguyên: "))

# Lấy chữ số hàng trăm
if abs(n) >= 100:  # Kiểm tra nếu số có ít nhất 3 chữ số
    hang_tram = abs(n) // 100  # Lấy phần nguyên khi chia cho 100
    print(f"Chữ số hàng trăm của {n} là: {hang_tram}")
else:
    print("Chữ số hàng trăm là: 0")
