import math
x = float(input("nhập giá trị x: "))
F = (-x+math.sqrt(x**2+4))/(x**4+1)**(1/7)
round(F, 2)
print("F(x) = ",F)