#Bài 9:
# Danh sách 1: Chỉ chứa số chẵn
lst = [2, 4, 6, 8, 10]
if all(x % 2 == 0 for x in lst):
    print("Tất cả các số trong danh sách đều là số chẵn.")
else:
    print("Danh sách chứa số lẻ!")

# Danh sách 2: Chứa số lẻ
lst2 = [2, 4, 5, 8]
if all(x % 2 == 0 for x in lst2):
    print("Tất cả các số trong danh sách đều là số chẵn.")
else:
    print("Danh sách chứa số lẻ!")