import re

def la_username_hop_le(username):
    return re.fullmatch(r'[A-Za-z0-9]+', username) is not None

def tao_email():
    danh_sach_email = []

    while True:
        ten = input("Nhập username (Enter để dừng): ")
        if ten == "":
            break

        if la_username_hop_le(ten):
            email = ten + "@companyname.com"
            danh_sach_email.append(email)
            print("Email đã tạo:", email)
        else:
            print("Lỗi: Username không hợp lệ. Chỉ dùng chữ cái và số, không dấu cách.")

    print("\nDanh sách email:")
    for e in danh_sach_email:
        print("-", e)

tao_email()