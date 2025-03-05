n=int(input('Nhap so nguyen n: '))
for i in range(2,n+1):
    ktNT=True
    squareRoot=int(i**0.5)
    for j in range(2,squareRoot+1):
        if (i%j==0):
            ktNT=False
            break
if ktNT:
    print(n,"La so nguyen to")
else:
    print(n,"Khong phai la so nguen to")
    #tim so ngyen to gan nhat
    for j in range(1,n):
        a=n-j
        b=n+j
        if a>1:
            for i in range(2,squareRoot+1):
                if a%i==0:
                    break
            else:
                print("So nguyen to gan nhat la:",a)
                break
        for i in range(2,squareRoot+1):
            if b%i==0:
                break
        else:
            print("So nguyen to gan nhat la:",b)
            break
