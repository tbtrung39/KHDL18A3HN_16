n = int(input("Nhập số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0!")
else:
    result = []
    temp_n = n  
    for i in range(2, n + 1):
        exponent = temp_n // i  
        factors = [i for _ in range(exponent) if temp_n % i == 0]  
        result.extend(factors)  
        temp_n = temp_n // (i ** len(factors)) 
    print("Phân tích thừa số nguyên tố:", " × ".join(map(str, result)))
