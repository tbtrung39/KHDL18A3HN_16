def kiem_tra_loi(chuoi):
    if not chuoi.isalpha():
        raise ValueError("Lỗi ký tự !!!")
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")
    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i + 1] == chuoi[i + 2] == chuoi[i + 3]:
            raise ValueError("Lỗi nhập lặp lại !!!")
    for i in range(len(chuoi) - 4):
        if chuoi[i] == chuoi[i + 1] == chuoi[i + 2] == chuoi[i + 3] == chuoi[i + 4]:
            raise ValueError("Lỗi nhập trùng lặp!!!")

while True:
    try:
        s = input("Nhập chuỗi ký tự: ")
        kiem_tra_loi(s)
        print("Nhập thành công!")
    except ValueError as e:
        print(e)
