list1 = input("Nhập danh sách list1: ").split(",")
list2 = input("Nhập danh sách list2: ").split(",")
dictionary = {list1[i]:list2[i] for i in range(min(len(list1),len(list2)))}
print(dictionary)
