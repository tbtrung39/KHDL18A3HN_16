a = int(input("Nhập số nguyên a:"))
b = int(input("Nhập số nguyên b:"))
while a == 0 or b == 0: 
    print("Hai số phải khác 0!!")
x = a 
y = b 
while y != 0:
    temp = y
    y = x%y
    x = temp
UCLN = x 
BCNN =(a*b)//UCLN
print("Bội chung nhỏ nhất của a và b là:",BCNN)