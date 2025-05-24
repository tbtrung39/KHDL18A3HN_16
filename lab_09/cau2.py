def giai_thua(n):
    if n==0:
        return 1
    else:
        return n*giai_thua(n-1)
    
n=int(input('nhap vao n:'))
result=giai_thua(n)
print('giai thua cua',n,'la',result)