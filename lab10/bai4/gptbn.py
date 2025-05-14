import math

def giai_pt_bac_nhat(a,b):
    if a==0:
        return "vo nghiem" if b!=0 else "vo so nghiem"
    return -b/a

def giai_pt_bac_hai(a,b,c):
    delta=b**2-4*a*c
    if delta < 0:
        return "phuong trinh vo nghiem"
    elif delta == 0:
        return f"nghiem kep = {-b/(2*a)}"
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return f"x1 = {x1}, x2 = {x2}"
    
