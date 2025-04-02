n = int( input(" Nhập số lượng tuple: "))
tuples_list = []
for _ in range(n):
    name, age, score = input(" Nhập tuple ( name age score): ").split()
    age = int(age)
    score = int(score)
    tuples_list.append( (name, age, score))
tuples_list.sort( key=lambda x: ( x, x, x))
print(" Danh sách sau khi sắp xếp: ")
for item in tuples_list:
    print(item)