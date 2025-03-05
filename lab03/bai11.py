h=int(input('Nhap so hang cua tam giac: '))
#tam giac a
k=2*h-2 #xac dinh khoang trang
for dong in range(1,h+1):
    for cot in range(1,k+1):
        print(" ",end="")
    for cot in range(1,2*dong):
        if cot==1 or cot==2*dong-1 or dong==h:
                print("*",end="")
        else:
                print(" ",end="")
    k=k-1
    print("\r")
#tam giac b
k=2*h-2 #xac dinh khoang trang
for dong in range(1,h+1):
    for cot in range(1,k+1):
        print(" ",end=" ")
    for cot in range(1,2*dong):
        if cot==1 or cot==2*dong-1 or dong==h:
                print("*",end=" ")
        else:
                print(" ",end=" ")
    k=k-1
    print("\r")
#tam giac c
k=2*h-2 #xac dinh khoang trang
for dong in range(1,h+1):
    for cot in range(1,k+1):
        print(" ",end=" ")
    for cot in range(1,2*dong):
        print("*",end=" ")
    else:
            print(" ",end=" ")
    k=k-1
    print("\r")
