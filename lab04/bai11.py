import os 
print('\n     MENU ĐỒ UỐNG       ')
while True:
    print("       MENU      ")
    print("[1] CAFE         ")
    print("[2] CAM VẮT      ")
    print("[3] NƯỚC ÉP CÀ RỐT")
    print("[4] NƯỚC LỌC     ")
    print("[5] NƯỚC DỪA     ")
    print("[0] Bấm 0 để thoát chương trình")
    print('___________________')
    chon = int(input("Chọn chức năng cần thực hiện: "))
    if chon == 1:
        print("Bạn đã chọn CAFE")
    if chon == 2:
        print("Bạn đã chọn CAM VẮT")
    if chon == 3:
        print("Bạn đã chọn NƯỚC ÉP CÀ RỐT")
    if chon == 4:
        print("Bạn đã chọn NƯỚC LỌC")
    if chon == 5:
        print("Bạn đã chọn NƯỚC DỪA")
    if chon == 0:
        break
    else:
        print("Chỉ chọn từ 1->5")
    tt =input("Nhâns bất kì đề tiếp tục,0 để thoát:")
    if tt ==0:
        break
    else: os.system('cls')