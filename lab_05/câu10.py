#câu10:cho trước hoặc nhập từ bàn phím 2 chuỗi ký tự Str....
s1 = input("nhap chuoi s1: ")
s2 = input("nhap chuoi s2: ")
max_len = ""
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        sub = s1[i:j]
        if sub in s2 and len(sub) > len(max_len):
            max_len = sub
print("chuoi con chung dai nhat", max_len)
