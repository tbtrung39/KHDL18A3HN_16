def find_solutions(n,x1,x2,x3):
    if x1+x2+x3==n:
        print(x1,x2,x3)
        return
    if x1+x2+x3<n:
        find_solutions(n,x1+1,x2,x3)
        find_solutions(n,x1,x2+1,x3)
        find_solutions(n,x1,x2,x3+1)
    
n=int(input('nhap so n:'))
print('cac nghiem cua phuong trinh n=x1+x2+x3 la:')
find_solutions(n,0,0,0)