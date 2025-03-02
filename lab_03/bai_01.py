n=int(input("nhap gia tri n:"))
tong = 0
tich_so_chan=1
for i in range(n+1):
    if i>0:
        tich_so_chan*=2*i
    mau_so=2*i+3
    tong+=tich_so_chan/mau_so
print("ket qua:",round(tong,3))