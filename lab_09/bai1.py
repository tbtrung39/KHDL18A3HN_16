def tim_max(a,b):
    if a>b:
        return a
    else:
        return b
def max_ba_so(a,b,c):
    return tim_max(a,tim_max(b,c))
a=int(input('nhap so thu nhat'))
b=int(input('nhap so thu hai'))
c=int(input('nhap so thu ba'))
kq=max_ba_so(a,b,c)
print('so lon nhat la:',kq)
