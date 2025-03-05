n = int(input("Nhập số nguyên dương n: "))

print(f"{n} = ", end="")

for i in range(2, n + 1): 
  for j in range(i, i+1):
        j % i == 0
        print(j, end="")
        n //= j
        if n > 1:
            print(" * ", end="")

print()