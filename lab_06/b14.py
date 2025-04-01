import re

def validate_password(password):
    if not 6 <= len(password) <= 12:
        return False
    patterns = [
        r'[a-z]',  # Chữ thường
        r'[0-9]',  # Số
        r'[A-Z]',  # Chữ hoa
        r'[$#@]'   # Ký tự đặc biệt
    ]
    return all(re.search(pattern, password) for pattern in patterns)

password = input("Nhập mật khẩu: ")
print("Mật khẩu hợp lệ!" if validate_password(password) else "Mật khẩu không hợp lệ!")