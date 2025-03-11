# Bài 2:
#a)
tong_a = 0
n = 1
while n <= 5: 
    tong_a = tong_a + 1/n
    n = n + 1
print("Tong a =", tong_a)

#b)
tong_b = 0
n = 2
while n <= 6: 
    phan_so = 1 / (n * (n + 1))
    tong_b = tong_b + phan_so
    n = n + 1
print("Tong b =", tong_b)

#c)
tong_c = 0
n = 2
while n <= 6:  
    can_bac_hai = n ** 0.5
    tong_c = tong_c + 1 / can_bac_hai
    n = n + 1
print("Tong c =", tong_c)