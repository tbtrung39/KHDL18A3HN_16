def luy_thua(a,n):
    if n==0:
        return 1
    return a*luy_thua(a,n-1)
a=int(input('nhap so a'))
n=int(input('nhap so mu a'))
kq=luy_thua(a,n)
print('a mu n la:',kq)