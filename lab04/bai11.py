import os 
print('CHƯƠNG TRÌNH GỌI ĐỒ UỐNG :') 
while True: 
    print("|                Menu chọn nước uống              |") 
    print("|[1] cafe                                         |") 
    print("|[2] cam vắt                                      |") 
    print("|[3] nước ép cà rốt                               |") 
    print("|[4] nước lọc                                     |") 
    print("|[0] nước dừa                                     |") 
    chon=int(input('Chọn chức năng cần thực hiện: ')) 
    if chon ==1: 
        print('Bạn đã chọn cafe. ') 
    elif chon==2: 
        print('Bạn đã chọn cam vắt. ') 
    elif chon==3: 
        print('Bạn đã chọn nước ép cà rốt. ')  
    elif chon==4: 
        print('Bạn đã chọn nước lọc. ') 
    elif chon==5: 
        print('Bạn đã chọn nước dừa. ') 
    elif chon==0: 
        break 
    else: 
        print('Chỉ chọn trong các số từ 1-4') 
    tt=input('Nhấn phím bất kỳ để tiếp tục, bấm số 0 để thoát.') 
    if tt=='0': 
        break 
    else: os.system('cls') 