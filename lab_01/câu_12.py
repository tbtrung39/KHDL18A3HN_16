import math
# Nhập vận tốc ban đầu
a = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))
# Tính toán thời gian để dừng
log4_5 = math.log2(5) / 2  # Tính log4(5) bằng công thức đổi cơ số
t = a / (2 * log4_5)  # Công thức tính thời gian
# Xuất kết quả (làm tròn 2 chữ số thập phân)
print(f"Thời gian ô tô dừng lại là: {round(t, 2)} giây")