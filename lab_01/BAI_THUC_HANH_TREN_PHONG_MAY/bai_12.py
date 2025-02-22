import math
# Nhập vận tốc ban đầu từ người dùng
van_toc_ban_dau = float(input("Nhập vận tốc ban đầu của ô tô (a): "))
# Tính toán
if van_toc_ban_dau < 0:
 print(input("Vận tốc ban đầu phải là một số không âm."))
thoi_gian = round((4 * van_toc_ban_dau) / math.log(5, 4),2)
# In kết quả
print("Thời gian ô tô đi được cho đến khi dừng:", thoi_gian, "giây")

