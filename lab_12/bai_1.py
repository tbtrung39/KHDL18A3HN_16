import math

def dien_tich_tam_giac():
    try:
        a = float(input('Nhap canh a: '))
        b = float(input('Nhap canh b: '))
        c = float(input('Nhap canh c: '))
        if a == 0 or b == 0 or c == 0:
            raise ZeroDivisionError('Khong the nhan voi 0.')
        A = [a, b, c]
        p = (a + b + b)/2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f'Dien tich tam giac la:', round(s, 3))
        return A
    except ZeroDivisionError as e:
        print('Loi:', e)
    except ValueError:
        print('Khong ra ket qua duoc.')
    except:
        print('Loi')

dien_tich_tam_giac()