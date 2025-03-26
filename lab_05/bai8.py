s=input("nhap chuoi 10 ky tu:")
if len(s) !=10:
    print("vui long nhap dung 10 ky tu")
else:
    a=s[2:7]
    print("a.chuoi con tu vi tri 3 den vi tri 7",a)
    b=s[:6]
    print("b.chuoi con 6 ky tu dau:",b)
    c=s[-4:]
    print("c.chuoi con 4 ky tu cuoi.",c)
    d=s[::-1]
    print("d.chuoi dao nguoc:",d)