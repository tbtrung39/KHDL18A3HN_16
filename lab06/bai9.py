lst = [2, 4, 6, 8, 10]
if (x % 2 == 0 for x in lst):
    print("Là số chẵn.")
else:
    print("Danh sách chứa số lẻ!")
lst2 = [2, 4, 5, 8]
if (x % 2 == 0 for x in lst2):
    print("Là số chẵn.")
else:
    print("Danh sách chứa số lẻ!")