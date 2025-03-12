import os
print(" CHƯƠNG TRÌNH GỌI ĐỒ UỐNG.")

while True:
    print("____________________________________")
    print("  Menu chọn nước uống:             ")
    print("|[1] Cafe             |")
    print("|[2] Cam vắt          |")
    print("|[3] Nước ép cà rốt   |")
    print("|[4] Nước lọc         |")
    print("|[5] Nước dừa         |")
    print("|[0] Thoát            |")
    print("|__________________________________|")

    chon = int(input("Chọn chức năng cần thực hiện(1-5): "))

    if chon == 1:
        print("Bạn đã chọn Cafe.")
    elif chon == 2:
        print("Bạn đã chọn Cam vắt.")
    elif chon == 3:
        print("Bạn đã chọn Nước ép cà rốt.")
    elif chon == 4:
        print("Bạn đã chọn Nước lọc.")
    elif chon == 5:
        print("Bạn đã chọn Nước dừa.")
    elif chon == 0:
        print("Thoát chương trình.")
        break
    else:
        print("Vui lòng chỉ chọn các số từ 0-5.")
    tt = input("nhấn phím bất kì để tiếp tục ,bấm số 0 để thoát")
    if tt==0:
        break
    else: os.system("cls")