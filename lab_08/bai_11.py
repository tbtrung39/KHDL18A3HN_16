def diem(toan, ly, hoa):
    return round((toan + ly + hoa)/3, 2)

hoten = input("Nhap ho ten: ")
while True:
    a = float(input("Nhap diem toan: "))
    b = float(input("Nhap diem ly: "))
    c = float(input("Nhap diem hoa: "))
    if 0 <= a <= 10 and 0 <= b <= 10 and 0 <= c <= 10:
        print(f'Ho ten: {hoten}')
        print(f'Diem toan: {a}|Diem ly: {b}|Diem hoa: {c}')
        print(f'Diem trung binh: {diem(a, b, c)}')
        break
    else:
        print("Nhap lai.")