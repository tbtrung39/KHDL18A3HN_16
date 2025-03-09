while True:
    print("MENU:")
    print("1. CAFE")
    print("2. Cam vắt")
    print("3. Cà rốt nước ép")
    print("4. Nước lọc")
    print("5. Nước dừa")
    print("0. Thoát")
    chose = input("Nhập lựa chọn: ")
    if chose == '1':
        print("You choose cafe")
    elif chose == '2':
        print("You choose orange juice")
    elif chose == '3':
        print("You choose carrot juice")
    elif chose == '4':
        print("You choose clean water")
    elif chose == '5':
        print("You choose kokonut da")
    elif chose == '0':
        print("Close")
        break
    else:
        print("kore wa requium da")