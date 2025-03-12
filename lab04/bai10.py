n=input('Nhap so thap phan: ')
i=0
while True:
    if i<len(n):
        j=int(n[i])
        if j==0:
            print('khong', end=' ')
        elif j==1:
            print('mot', end=' ')
        elif j==2:
            print('hai', end=' ')
        elif j==3:
            print('ba', end=' ')
        elif j==4:
            print('bon', end=' ')
        elif j==5:
            print('nam', end=' ')
        elif j==6:
            print('sau', end=' ')
        elif j==7:
            print('bay', end=' ')
        elif j==8:
            print('tam', end=' ')
        elif j==9:
            print('chin', end=' ')
        i=i+1
    else:
        break
print()
        