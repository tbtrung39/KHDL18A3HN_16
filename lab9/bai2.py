def ucln (a, b):
    if b==0:
        return a
    else:
        return ucln(b, a%b)
    
def ucln_list(numbers):
    if len(numbers)==1:
        return numbers[0]
    else:
        return ucln(numbers[0], ucln_list(numbers[1:]))
    
n=int(input("Nhap so luong phan tu: "))
numbers=[]
for _ in range(n):
    numbers.append(int(input("Nhap so: ")))

#tinh ucln
result=ucln_list(numbers)
print("Uoc chung lon nhat la:", result)