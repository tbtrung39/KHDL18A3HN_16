import math

# Danh sách cách đọc các chữ số
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

# Nhập số nguyên có ba chữ số
n = int(input("Nhập số nguyên có ba chữ số: "))

# Kiểm tra nếu số không phải ba chữ số
if n < 100 or n > 999:
    print("Vui lòng nhập số có đúng ba chữ số.")
else:
    tram = n // 100
    chuc = (n // 10) % 10
    don_vi = n % 10
    
    # Xây dựng cách đọc số
    ket_qua = f"{chu_so[tram]} trăm"
    
    if chuc == 0:
        if don_vi != 0:
            ket_qua += f" linh {chu_so[don_vi]}"
    elif chuc == 1:
        ket_qua += f" mười {chu_so[don_vi]}"
    else:
        ket_qua += f" {chu_so[chuc]} mươi"
        if don_vi == 1:
            ket_qua += " mốt"
        elif don_vi == 5:
            ket_qua += " lăm"
        elif don_vi != 0:
            ket_qua += f" {chu_so[don_vi]}"
    
    print(f"Cách đọc: {ket_qua}")
