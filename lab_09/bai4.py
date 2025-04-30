def hoan_vi(day, trai, phai):
    if trai == phai:
        print(day)
    else:
        for i in range(trai, phai + 1):
            day[trai], day[i] = day[i], day[trai]
            hoan_vi(day, trai + 1, phai)
            day[trai], day[i] = day[i], day[trai]
n = int(input("Nhap so tu nhien n: "))
day = [i for i in range(1, n + 1)]
print("Cac hoan vi cua day:", day)
hoan_vi(day, 0, n - 1)

