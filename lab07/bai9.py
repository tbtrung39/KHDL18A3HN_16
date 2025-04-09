n = int(input("Nhập số tự nhiên n từ bàn phím: "))
A = set()
B = set()
for i in range(2,n+1):
    kt_so_nt = True
    for j in range(2,int(i**0.5)+1):
        if i % j == 0: 
            kt_so_nt = False
            break
        if kt_so_nt:
            if n % i ==0:
                A.add(i)
            elif i<n:
                B.add(i)
print("A là tập các số nguyên tố là ước của n: ",A)
print("B là tập hợp các số nguyên tố nhỏ hơn n và không là ướcc của n: ",B)