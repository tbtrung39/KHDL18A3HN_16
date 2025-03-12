n=int(input("nhap mot so nguyen duong: "))
tong=0
while n!=0:
    tong+=n%10
    n//=10
print("tong cac chu so la: ", tong)