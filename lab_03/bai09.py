#cau aa
n=int(input("nhập n="))
if n<0:
    print("số không hợp lệ vui lòng nhập lại")
else:
    tong=0
    for i in range(1,n+1,1):
        tong= tong + i**2
    print("tổng = ",tong)




#cau b:
#cau c
n=int(input("nhập n="))
if n<0:
    print("số không hợp lệ vui lòng nhập lại")
else:
    tong=0
    for i in range(1,n+1,2):
        tong+=i**3 
    print("tổng",tong)




#cau c
#cau c
n=int(input("nhập n="))
if n<0:
    print("số không hợp lệ vui lòng nhập lại")
else:
    tong=0
    for i in range(2,n+1,2):
        tong+=i**4  
    print("tổng",tong)