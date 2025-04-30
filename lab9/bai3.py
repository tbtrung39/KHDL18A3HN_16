def sum_power_of_2(n):
    if n==2:
        return 2
    else:
        return 2**n + sum_power_of_2(n-1)
    
n=int(input("Nhap so n: "))
result=sum-sum_power_of_2(n)
print("Tong luy thua cua 2 la:", result)