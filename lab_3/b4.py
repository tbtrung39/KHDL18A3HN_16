n = int(input("nhập số n: "))
for num in range(2, n+1):
    la_nguyen_to = True 
    for uoc in range(2, int(num **0.5)+1):
        if num % uoc ==0:
            la_nguyen_to = False
            break 
        if la_nguyen_to:
            print(num, end="")