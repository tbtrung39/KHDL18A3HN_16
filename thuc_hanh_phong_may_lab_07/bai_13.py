#Bài 13:
s = input("Nhập chuỗi ký tự: ")
d = {s[i:j]: s.count(s[i:j]) 
     for i in range(len(s)) 
     for j in range(i + 1, len(s) + 1) 
     if s[i:j].strip()}

print(d)