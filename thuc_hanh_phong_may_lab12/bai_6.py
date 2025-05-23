def la_username_hop_le(username):
    return username.isalnum()

ds_email = []

try:
    username = input("Nhập username: ")
    if not la_username_hop_le(username):
        raise ValueError("Lỗi: Username chỉ được chứa chữ và số, không có dấu cách hoặc ký tự đặc biệt.")
    email = username + "@companyname.com"
    ds_email.append(email)
    print("Email đã tạo:", email)
except ValueError as e:
    print(e)
