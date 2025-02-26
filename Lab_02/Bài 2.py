import math
a, b, c= map( float, input(" Nhập những hệ số a, b, c lần lượt là ").split(","))
if a == 0:
    if b == 0:
        if c == 0:
            print(" Phương trình có vô số nghiệm")
        else:
            print (" Phương trình vô nghiệm")
    else:
           print (" Phương trình có nghiệm duy nhất: x = ", -c / b)
else:
    delta= b** 2- 4* a* c
    if delta< 0:
        print(" Phương trình vô nghiệm")
    elif delta== 0:
        print(" Phương trình có nghiệm kép: x= ", -b / (2 * a))
    else:
        print(" Phương trình có hai nghiệm phân biệt: x1= ", (-b + math.sqrt(delta)) / (2 * a), " và x2= ", (-b - math.sqrt(delta)) / (2 * a))



