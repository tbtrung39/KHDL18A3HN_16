so_tien = 0
while True:
    giao_dich = input("Nhập giao dịch: ")
    if giao_dich.lower() == 'q':
        break
    elements = giao_dich.split()
    if len(elements) != 2:
        print("Định dạng giao dịch không đúng. Vui lòng nhập lại. ")
        continue
    loai_giao_dich = elements.upper()
    if not elements.isdigit():
        print("Số tiền không hợp lệ. Vui lòng nhập lại.")
        continue
    so_tien_giao_dich = int(elements)
    if loai_giao_dich == 'D':
        so_tien += so_tien_giao_dich
    elif loai_giao_dich == 'W':
        so_tien -= so_tien_giao_dich
    else:
        print("Giao dịch không hợp lệ. Vui lòng nhập lại. ")
print("Số tiền trong tài khoản: ", so_tien)