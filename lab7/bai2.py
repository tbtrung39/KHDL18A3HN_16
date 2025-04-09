Numbers=list(map(int, input("Nhap so tu nhien: ").split()))
A=set(Numbers)
count_dict={}
for Num in Numbers:
    count_dict[Num]=count_dict.get(Num,0)+1
print("Danh sach Numbers la:", Numbers)
print("Tap hop A:", A)