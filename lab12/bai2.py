def kiem_tra_chuoi(chuoi):
    # Kiểm tra ký tự không phải là chữ cái
    for ky_tu in chuoi:
        if not ky_tu.isalpha():
            raise ValueError("Lỗi ký tự !!!")
    
    # Kiểm tra 2 ký tự liên tiếp giống nhau
    for i in range(len(chuoi) - 1):
        if chuoi[i] == chuoi[i + 1]:
            raise ValueError("Lỗi nhập liệu !!!")
    
    # Kiểm tra 4 ký tự liên tiếp giống nhau
    for i in range(len(chuoi) - 3):
        if chuoi[i] == chuoi[i + 1] == chuoi[i + 2] == chuoi[i + 3]:
            raise ValueError("Lỗi nhập lặp lại !!!")
    
    # Kiểm tra 5 từ giống nhau liên tiếp
    tu = chuoi.split()
    for i in range(len(tu) - 4):
        if tu[i] == tu[i + 1] == tu[i + 2] == tu[i + 3] == tu[i + 4]:
            raise ValueError("Lỗi nhập trùng lặp!!!")

while True:
    try:
        chuoi = input("Nhập một chuỗi ký tự: ")
        kiem_tra_chuoi(chuoi)
        print("Chuỗi nhập vào hợp lệ.")

    except ValueError as e:
        print("Lỗi:", e)