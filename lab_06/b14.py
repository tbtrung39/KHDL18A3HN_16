import re
password = input("Nhập mật khẩu: ")
if 6 <= len(password) <= 12 and all(re.search(p, password) for p in [r'[a-z]', r'[0-9]', r'[A-Z]', r'[$#@]']):
    print("Mật khẩu hợp lệ!")
else:
    print("Mật khẩu không hợp lệ!")
