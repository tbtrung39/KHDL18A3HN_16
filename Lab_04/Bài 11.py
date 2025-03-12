import os
while True:
    print(" ________ MENU________")
    print(" 1. Cafe")
    print(" 2. Cam vắt")
    print(" 3. Nước ép cà rốt")
    print(" 4. Nước lọc")
    print(" 5. Nước dừa")
    print(" 6. Thoát")
    lua_chon= int(input(" Nhập lựa chọn: "))
    if lua_chon == 1:
        print("Bạn đã chọn Cafe.")
    elif lua_chon == 2:
        print("Bạn đã chọn Cam vắt.")
    elif lua_chon == 3:
        print("Bạn đã chọn Nước ép cà rốt.")
    elif lua_chon == 4:
        print("Bạn đã chọn Nước lọc.")
    elif lua_chon == 5:
        print("Bạn đã chọn Nước dừa.")
    elif lua_chon == 6:
        print("Thoát.")
        break
    else:
        print(" Nhập các số từ 1- 6.")
    tt = int( input(" Nhấn phím bất kì để tiếp tục ,bấm số 0 để thoát: "))
    if tt==0:
        break
    else: 
        os.system("cls")