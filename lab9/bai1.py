def find_max(a, b, c):
    if a>b:
        max_ab=a
    else:
        max_ab=b

    #so sanh max_ab voi c
    if max_ab>c:
        return max_ab
    else:
        return c
    
x=int(input("Nhap so thu nhat: "))
y=int(input("Nhap so thu hai: "))
z=int(input("Nhap so thu ba: "))
result=find_max(x, y, z)
print("So lon nhat la:", result)