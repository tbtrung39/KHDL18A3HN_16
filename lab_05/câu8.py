#câu8:cho trước xâu str là 1 đoạn văn bản hoàn chỉnh (có thể bao gồm nhiều dòng)
s1 = input("nhap chuoi s1: ")
s2 = input("nhap chuoi s2: ")
s = ""
min_len = min(len(s1),len(s2))
for i in range(min_len):
    s += s1[i]+s2[i]
s += s1[min_len:]+s2[min_len:]
print("chuoi sau khi tron:", s)