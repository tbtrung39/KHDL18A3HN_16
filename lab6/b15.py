numbers = list(map(int, input("Nhập các số cách nhau bằng dấu phẩy: ").split(',')))
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Tổng các số chẵn:", even_sum)