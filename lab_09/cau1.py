def cap_so_nhan(n):
    if n==1:
        return
    else:
        return 2*cap_so_nhan(n-1)
    
n=int(input('nhap vao so n:'))
result=cap_so_nhan(n)
print('so hang thu',n,'cua cap so nhan la',result)