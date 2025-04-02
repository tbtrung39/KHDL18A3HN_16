so_du = 0
while True:
    giao_dich = input("Nhập giao dịch (hoặc gõ 'N' để dừng): ").strip()
    # Kiểm tra nếu người dùng muốn dừng
    if giao_dich == 'N':
        break    
    # Xử lý giao dịch gửi tiền (D) và rút tiền (W)
    try:
        # Nếu là giao dịch gửi tiền
        if giao_dich.startswith('D'):
            so_tien = int(giao_dich.split()[1].replace('.', ''))  # Lấy số tiền gửi
            so_du += so_tien
        # Nếu là giao dịch rút tiền
        elif giao_dich.startswith('W'):
            so_tien = int(giao_dich.split()[1].replace('.', ''))  # Lấy số tiền rút
            so_du -= so_tien
    except (IndexError, ValueError):  # Kiểm tra lỗi nếu dữ liệu không hợp lệ
        print("Giao dịch không hợp lệ, vui lòng nhập lại.")
# In số dư tài khoản cuối cùng
print("Số tiền thực trong tài khoản là:", so_du)
