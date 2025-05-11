def loaibo(n):
    kytu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    if n in kytu:
        return n
    else:
        return 'Nhap lai'

def chuoichotruoc(n):
    if loaibo(n):
        if n == int(n, 2):
            print("Hệ cơ số 2")
        elif n == int(n, 8):
            print('Hệ cơ số 8')
        elif n == int(n, 10):
            print('Hệ cơ số 10')
        elif n == int(n, 16):
            print('Hệ cơ số 16')

def nhiphansangthapphan(n):
    return int(n, 2)

def batphansangthapphan(n):
    return int(n, 8)

def thaplucphansangthappahn(n):
    return int(n, 16)