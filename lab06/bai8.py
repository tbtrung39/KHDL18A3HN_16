n = int(input("Nhập n: "))
# Tạo danh sách Fibonacci bằng list comprehension
fibonaci = [0, 1]
[fibonaci.append(fibonaci[-1] + fibonaci[-2]) for _ in range(n - 1)]
# In dãy Fibonacci, các phần tử cách nhau bằng dấu ","
print(", ".join(map(str, fibonaci)))
