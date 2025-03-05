n=int(input("nhap so nguyen n: "))
for i in range(2,n+1):
    khTN=True
    squareRoot=int(i**0.5)
    for j in range(2,squareRoot+1):
        if (i%j==0):
            ktNT=False
            break
if ktNT:
    print(n, "la so nguyen to")
else:
    print(n, "khong phai la so nguyen to")
    # tim so nguyen to gan nhat
    for i in range(1,n):
        a=n-j
        b=n+j
        if a>1:
            for i in range(2,squareRoot+1):
                if a%i==0:
                    break
            else:
                print("so nguyen gan nhat la: ",a)
                break
        for i in range(2,squareRoot+1):
            if b%i==0:
                break
        else:
            print("so nguyen gan nhat la: ",b)
            break 