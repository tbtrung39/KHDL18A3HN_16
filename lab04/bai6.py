n = int(input("nhap so: "))

if n == 0:
    print("khong")
else:
    a = ""
    while n > 0:
        du = n % 10  # Lay chu so cuoi cung
        n = n // 10  # Bo chu so cuoi cung

        if du == 0:
            a = "khong " + a
        elif du == 1:
            a = "mot " + a
        elif du == 2:
            a = "hai " + a
        elif du == 3:
            a = "ba " + a
        elif du == 4:
            a = "bon " + a
        elif du == 5:
            a = "nam " + a
        elif du == 6:
            a = "sau " + a
        elif du == 7:
            a = "bay " + a
        elif du == 8:
            a = "tam " + a
        elif du == 9:
            a = "chin " + a

    print("ket qua: ", a.strip())  # In ra ket qua