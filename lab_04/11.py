import os
print('\n CHƯƠNG TRÌNH TÍNH TOÁN CỘNG,TRỪ, NHÂN, CHIA.')
while True:
    print(' _________________________________________________')
    print("|               Menu chọn chức năng:              |")
    print("|                1. Cafe                          |")
    print("|                2. Cam ép                        |")
    print("|                3. Nước ép cà rốt                |")
    print("|                4. Nước lọc.                     |")
    print("|                5. Nước dừa.                     |")
    print("|                0. Bấm số 0 để thoát             |")
    print('|_________________________________________________|')
    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon ==1:
        print('Bạn đã chọn Cafe.')
    elif chon==2:
        print('Bạn đã chọn Cam ép.')
    elif chon==3:
        print('Bạn đã chọn Nước ép cà rốt')
    elif chon==4:
        print('Bạn đã chọn Nước lọc')
    elif chon==4:
        print('Bạn đã chọn Nước dừa')
    elif chon==0:
        break
    else:
        print('Chỉ chọn trong các số từ 1-5')
    tt=input('Nhấn phím bất kỳ để tiếp tục, bấm số 0 để thoát.')
    if tt=='0':
        break
    else: os.system('cls')