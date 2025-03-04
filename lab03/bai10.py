n = int(input("Nhập số nguyên dương n= "))
for i in range(2, n + 1):
    for a in range(n // i): 
        if n % i == 0:
            print("Dạng phân tích của thừa số nguyên tố:",i)
            n //= i  
        else:
            break
