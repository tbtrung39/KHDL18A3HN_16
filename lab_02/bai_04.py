n = int(input("Nhập vào một số nguyên: "))
# Lấy giá trị tuyệt đối để xử lý cả số âm
n = abs(n)
# Lấy chữ số hàng trăm
so_hang_tram = (n // 100) % 10
print(f"Chữ số hàng trăm là: {so_hang_tram}")
