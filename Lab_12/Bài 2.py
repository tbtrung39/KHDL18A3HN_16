def nhap_ky_tu():
    try:
        s = input(" Nhập chuỗi ký tự: ")
        if not all(c.isalpha() for c in s):
            raise ValueError(" Lỗi ký tự. ")
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                raise ValueError(" Lỗi nhập liệu. ")
        for i in range(len(s) - 4):
            if len(set(s[i:i+5])) == 1:
                raise ValueError(" Lỗi nhập trùng lặp. ")
        print(" Dữ liệu hợp lệ: ", s)
    except ValueError as e:
        print(e)
        print(" Vui lòng nhập lại. ")
        nhap_ky_tu()
nhap_ky_tu()