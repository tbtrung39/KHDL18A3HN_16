def lay_chu_so_hang_tram(n):
    # Lấy giá trị tuyệt đối của n để xử lý cả số âm
    n = abs(n)
    # Kiểm tra số có ít nhất 3 chữ số
    if n < 100:
        return 0
    else:
        # Lấy chữ số hàng trăm
        return (n // 100) % 10
# Nhập số nguyên từ người dùng
try:
    so_nguyen = int(input("Nhập vào một số nguyên: "))
    chu_so_hang_tram = lay_chu_so_hang_tram(so_nguyen)
    print(f"Chữ số hàng trăm của số {so_nguyen} là: {chu_so_hang_tram}.")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")