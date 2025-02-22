import math 
x = float(input("Nhập giá trị x: ")) 
fx = (math.log(x) / math.log(4)) + (math.log(2) / math.log(x)) 
fx = round(fx, 2)  # làm tròn 
print("Giá trị của biểu thức đã cho là:", fx) 