import math

def la_tam_giac(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        print("Là tam giác")
        return True
    print("Không phải tam giác")
    return False

def chu_vi_tam_giac(a, b, c):
    return a + b + c

def dien_tich_tam_giac(a, b, c):
    nua_chu_vi = chu_vi_tam_giac(a, b, c) / 2
    dien_tich = math.sqrt(
        nua_chu_vi * 
        (nua_chu_vi - a) * 
        (nua_chu_vi - b) * 
        (nua_chu_vi - c)
    )
    return dien_tich