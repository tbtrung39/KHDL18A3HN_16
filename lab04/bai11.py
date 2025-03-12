import os
print('\n CHUONG TRINH GOI DO UONG.')
while True:
    print(' ______________________________________')
    print("|      Menu chon cac loai do uong       |")
    print("|[1] Cafe                               |")
    print("|[2] Cam vat                            |")
    print("|[3] Nuoc ep ca rot                     |")
    print("|[4] Nuoc loc                           |")
    print("|[5] Nuoc dua                           |")
    print("|[0] Bam so 0 de thoat                  |")

    chon=int(input('Chon loai do uong: '))
    if chon==1:
        print('Ban da chon Cafe.')
    elif chon==2:
        print('Ban da chon Cam vat.')
    elif chon==3:
        print('Ban da chon Nuoc ep ca rot.')
    elif chon==4:
        print('Ban da chon Nuoc loc.')
    elif chon==5:
        print('Ban da chon Nuoc dua.')
    elif chon==0:
        break
    else:
        print('Chi chon trong cac so tu 1-5')
    tt=input('Nhan phim bat ky de tiep tuc, bam so 0 de thoat.')
    if tt=='0':
        break
    else: os.system('cls')

