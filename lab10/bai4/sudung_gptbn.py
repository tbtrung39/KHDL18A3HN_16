import gptbn

# giai phuong trinh bac nhat: ax+b=0
a=float(input("nhap a: "))
b=float(input("nhap b: "))
print("ket qua phuong trinh bac nhat: ", gptbn.giai_pt_bac_nhat(a,b))

# giai phuong trinh bac hai: ax^2+bx+c=0
a=float(input("nhap a: "))
b=float(input("nhap b: "))
c=float(input("nhap c: "))
print("ket qua phuong trinh bac hai: ", gptbn.giai_pt_bac_hai(a,b,c))