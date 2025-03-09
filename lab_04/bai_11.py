import os
print("\n CHƯƠNG TRÌNH GỌI ĐỒ UỐNG ") 
while True:
# Hiển thị menu chọn đồ uống
    print(' _________________________________________________')
    print("| Menu chọn đồ uống: |") 
    print("|[1] Cafe |") 
    print("|[2] Cam vắt |")
    print("|[3] Nước ép cà rốt |") 
    print("|[4] Nước lọc |") 
    print("|[5] Nước dừa |")
    print("|[0] Bấm 0 để thoát |")
    print('|_________________________________________________|') 
    chon=int(input('Chọn đồ uống '))
    if chon ==1:
        print('Bạn đã chọn Cafe')
    elif chon==2:
        print('Bạn đã chọn cam vắt.') 
    elif chon==3:
        print('Bạn đã chọn Nước ép cà rốt')
    elif chon==4:
        print('Bạn đã chọn Nước lọc')
    elif chon==5:
        print('Bạn đã chọn Nước dừa')
    elif chon==0: 
        break
    else:
        print('Chỉ chọn trong các số từ 1-4') 
        #break
    tt=input('Nhấn phím bất kỳ để tiếp tục, bấm số 0 để thoát.')
    if tt=='0': 
        break
    else: os.system('cls')