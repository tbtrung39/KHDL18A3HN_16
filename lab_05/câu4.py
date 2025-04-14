# cho trước 2 chuỗi ký tự Str1, Str2(có thể từ bàn phím )....
S = input("nhap chuoi 10 ky tu: ")
if len(S) !=10:
    print("vui long nhap dung 10 ky tu. ")
else:
    a = S[2:7]
    print("a.chuoi con tu vi tri 3 den vi tri 7", a)
    b = S[:6]
    print("b.chuoi con 6 ky tu tu dau", b)
    c = S[-4:]
    print("c.chuoi con 4 ky tu tu cuoi", c)
    d = S[::-1]
    print("d.chuoi dao nguoc", d)