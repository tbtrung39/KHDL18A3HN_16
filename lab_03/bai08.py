n=int(input("nhập n="))
if n<0:
    print("số không hợp lệ vui lòng nhập lại")
else:
    tong=0
    for i in range(1,n+1,1):
        tong+=i
    print("tổng",tong)

#cau b
n=int(input("nhập n="))
if n<0:
    print("số không hợp lệ vui lòng nhập lại")
else:
    tong=0
    for i in range(1,n+1,2):
        tong+=i
    print("tổng",tong)

#cau c
n=int(input("nhập n="))
if n<0:
    print("số không hợp lệ vui lòng nhập lại")
else:
    tong=0
    for i in range(2,n+1,2):
        tong+=i
    print("tổng",tong)