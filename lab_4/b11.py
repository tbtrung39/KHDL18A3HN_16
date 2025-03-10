import os 
print("\n       CHƯƠNG TRÌNH GỌI ĐỒ UỐNG      ")
while True:
    # hiển thị menu 
    print("___________________________________")
    print("|             Menu đồ uống         ")
    print("|[1] Cafe                         |")
    print("|[2] Cam vắt                      |")
    print("|[3] Nước ép cà rốt               |")
    print("|[4] Nước lọc                     |")
    print("|[5] Nước dừa                     |")
    chon = int(input("chọn đồ uống: "))
    if chon ==1: 
        print("bạn đã chọn cafe ")
    elif chon ==2:
        print("bạn đã chọn cam vắt")
    elif chon ==3: 
        print("bạn đã chọn nước ép cà rốt")
    elif chon ==4: 
        print("bạn đã chọn nước lọc")
    elif chon ==5: 
        print("bạn đã chọn nước dừa")
        break 
    else:
        print("chỉ chọn trong các số từ 1-5")
else:
     os.system("cls")