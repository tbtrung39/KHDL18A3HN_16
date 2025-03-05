n=int(input("nhap so nguyen n: "))
for i in range(2,n+1):
    ktNT=True
    squareRoot=int(i**0.5)
    for j in range(2,squareRoot+1):
        if (i%j==0):
            ktTN=False
    if ktNT:
        print(i,end=' ')
print()