a= [ 2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong= 0
dem= 0
tong1= 0
position= 0
position1= 0
max= a[0]
position2= 0
for i in a:
    tong= tong+ i
print(" Tổng của những phần tử: ", tong)
for j in a:
    if j > 0:
        dem= dem+ 1
        tong1= tong1+ j
print(" Số những số hạng dương: ", dem)
print(" Tổng của những số hạng dương: ", tong1)
for t in range(len(a)):
    if a[ t] < 0:
        position= t
        break
print(" Vị trí của phần tử âm đầu tiên: ", position)
for k in range(len(a) - 1, -1, -1):
    if a[k] > 0:
        position1= k
        break
print(" Vị trí của phần tử dương cuối cùng: ", position1)
for g in range(len(a)):
    if a[g]> max:
        max= a[g]
        position2= g
print(" Phần tử lớn nhất: ", max)
print(" Vị trí của phần tử lớn nhất: ", position2)

        

