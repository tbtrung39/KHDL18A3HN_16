numbers = list( map( int, input("Nhập các số nguyên: ").split()))
assert all(num % 2 == 0 for num in numbers), "Danh sách chứa số lẻ!"
print("Tất cả các số trong danh sách đều là số chẵn.")