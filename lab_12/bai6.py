try:
    username = input("Nhập username: ")
    if not username.isalnum():
        raise ValueError("Username chỉ được gồm chữ và số.")
    email = username + "@companyname.com"
    print("Email:", email)
except ValueError as e:
    print("Lỗi:", e)
