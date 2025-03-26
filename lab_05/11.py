n = input('Nhập số nhị phân: ')
binary = True
for i in n:
     if i != '0' and i != '1':
         binary = False
         break
 
if binary:
     decimal = 0
     for j in range(len(n)):
         decimal += int(str(j)) * (2**(len(n) - j - 1))
     print("Sô thập phân tương ứng là:", decimal)
else:
     print("Chuỗi ký tự không phải là nhị phân")