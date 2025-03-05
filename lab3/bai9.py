n=int(input("nhap mot so nguyen duong n: "))
S4=0
S5=0
S6=0
if n <= 0:
    print("nhap sai vui long nhap lai!")
else:
    # tính S4
    for i in range(1,n+1):
        S4=S4+i**2
    print("S4 = ",S4) 
    # tính S5
    for i in range(1,2*n+2,2):
        S5=S5+i**3
    print("S5 = ",S5)
    # tinh S6
    for i in range(2,2*n+1,2):
        S6=S6+i**4
    print("S6 = ",S6)