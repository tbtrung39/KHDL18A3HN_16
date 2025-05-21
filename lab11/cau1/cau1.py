# Mở tệp và đọc nội dung
with open('lab11/cau1/dayso.dat', 'r') as file:
    data = file.read()
numbers = list(map(int, data.split()))
day_so_le = [x for x in numbers if x % 2 == 1]
tinh_tong_so_le = sum(day_so_le)
print("Tổng các số lẻ trong dãy là:",tinh_tong_so_le)
 