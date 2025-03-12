import os
print("\n CHUONG TRINH CONG, TRU, NHAN, CHIA.")
while True:
    # hien thi menu chon chuc nang
    print("|                      MENU CHON DO AN                     |")
    print("|[1] cafe                                                  |")
    print("|[2] cam vat                                               |")
    print("|[3] nuoc ep ca rot                                        |")
    print("|[4] nuoc loc                                              |")
    print("|[5] nuoc dua                                              |")
    print("|[0] bam so 0 de thoat                                     |")
    print("|__________________________________________________________|")

    chon=int(input("chon do an: "))
    if chon==1:
        print("ban da chon cafe")
    elif chon==2:
        print("ban da chon cam vat") 
    elif chon==3:
        print("ban da chon nuoc ep ca rot") 
    elif chon==4:
        print("ban da chon nuoc loc") 
    elif chon==5:
        print("ban da chon nuoc dua") 
    elif chon==0:
        break 
    else:
        print("chi chon trong cac so tu 0-5")
        
    tt=input("nhan phim bat ki de tiep tuc, nhan phim 0 de thoat.")
    if tt==0:
        break
    else:
        os.system('cls')