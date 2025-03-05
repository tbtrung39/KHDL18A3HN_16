n=int(input("nhap mot so nguyen duong n: "))
S1=0
S2=0
S3=0
if n <= 0:
    print("nhap sai vui long nhap lai!")
else:
    for i in range(1, n + 1):
        S1 += i

    for i in range(1, 2 * n + 2, 2):
        S2 += i

    for i in range(2, 2 * n + 1, 2):
        S3 += i
    print(f"S1 = {S1}")
    print(f"S2 = {S2}")
    print(f"S3 = {S3}")