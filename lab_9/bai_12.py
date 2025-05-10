def chicken(n):
    if n % 2 == 0:
        return f'{round(n/2)}'
    else:
        return chicken(n - 1)

def dog(n):
    if n % 4 == 0:
        return f'{round(n/4)}'
    else:
        return dog(n - 1)

n = int(input("Nhap so luong: "))
print('Ga co:', chicken(n), 'con')
print('Cho co:', dog(n), 'con')