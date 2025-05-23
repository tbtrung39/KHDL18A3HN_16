def nhap_ky_tu():
    try:
        s = input("Nhập chuỗi ký tự: ")

        if not all(c.isalpha() for c in s):
            raise ValueError("Lỗi ký tự !!!")  # Chứa ký tự không phải chữ cái

        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                raise ValueError("Lỗi nhập liệu !!!")  # Hai ký tự liền giống nhau

        for i in range(len(s) - 4):
            if len(set(s[i:i+5])) == 1:
                raise ValueError("Lỗi nhập trùng lặp !!!")  # 5 ký tự giống nhau liên tiếp

        print("Dữ liệu hợp lệ:", s)

    except ValueError as e:
        print(e)
        print("Vui lòng nhập lại.")
        nhap_ky_tu()  # Gọi lại để người dùng nhập tiếp

nhap_ky_tu()