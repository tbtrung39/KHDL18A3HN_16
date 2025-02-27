n = int(input("nhập n "))
tong =1
tich = 1
phan_so=2/3
for i in range(1,n+1):
    tich = tich*((2*i)/(2*i+1))
    tong=tong+phan_so*tich
    ket_qua=int(tong*1000)/1000
    print("kết quả = ",ket_qua)   