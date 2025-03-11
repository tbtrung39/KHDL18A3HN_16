#Bài 11:
import os
print('\n CHƯƠNG TRÌNH GỌI ĐỒ UỐNG.')
while True:
    print(' __________________________________________________')
    print("| Menu chọn chức năng:                            |")
    print("|[1] Bạn đã chọn Cafe                             |")
    print("|[2] Bạn đã chọn Nước cam vắt                     |")
    print("|[3] Bạn đã chọn Nước ép cà rốt                   |")
    print("|[4] Bạn đã chọn Nước lọc                         |")
    print("|[5] Bạn đã chọn Nước dừa                         |")
    print("|[0] Bấm số 0 để thoát                            |")
    print('|_________________________________________________|')
    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon == 1:
        print('Bạn đã chọn Cafe.')
    elif chon == 2:
        print('Bạn đã chọn Nước cam vắt.')
    elif chon == 3:
        print('Bạn đã chọn Nước ép cà rốt')
    elif chon == 4:
        print('Bạn đã chọn Nước lọc')
    elif chon == 5:
        print("Bạn đã chọn Nước dừa")
    elif chon == 0:
        break
    else:
        print('Chỉ chọn trong các số từ 1-4')
    tt=input('Nhấn phím bất kỳ để tiếp tục, bấm số 0 để thoát.')
    if tt=='0':
        break
    else: 
        os.system('cls')

