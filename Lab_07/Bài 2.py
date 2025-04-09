number = input("Nhập những số tự nhiên( cách nhau bởi dấu cách) : ")
Numbers= list(map(int, number.split()))
A = set(Numbers)
print('Danh sách Numbers: ', Numbers)
print("Tập hợp A: ", A)

