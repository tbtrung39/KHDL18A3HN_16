numbers = list(map(int, input("Nhập các số cách nhau bằng dấu phẩy: ").split(',')))
unique_numbers = sorted(list(set(numbers)), reverse=True)
second_largest = unique_numbers[1] if len(unique_numbers) >= 2 else "Không có"
print("Số lớn thứ hai:", second_largest)
