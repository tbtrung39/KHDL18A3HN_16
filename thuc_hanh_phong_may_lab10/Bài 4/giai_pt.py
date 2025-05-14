import math

def giai_phuong_trinh_bac1(a, b):
    if a == 0:
        return "Vô nghiệm" if b != 0 else "Vô số nghiệm"
    return -b / a

def giai_phuong_trinh_bac2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Vô nghiệm"
    elif delta == 0:
        return -b / (2*a)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
