#a
def sum_1_to_n(n):
    if n==1:
        return 1
    else:
        return n+sum_1_to_n(n-1)

n=int(input('nhap so tu nhien n:'))
result=sum_1_to_n(n)
print('tong s1=1+2+...+n=',result)
#b
def sum_even_numbers(n):
    if n==1:
        return 2
    else:
        return 2*n + sum_even_numbers(n-1)

n=int(input('nhap so tu nhien n:'))
result=sum_even_numbers(n)
print('tong s2=2+4=...+2n=',result)

#c,
def sum_odd_numbers(n):
    if n==1:
        return 1
    else:
        return 2*n-1+sum_odd_numbers(n-1)

n=int(input('nhap so tu nhien n:'))
result=sum_odd_numbers(n)
print('tong s3=1+3+5=..+2n-1=',result)