n= int(input(" Nhập số nguyên dương n: "))
S4= S5= S6= 0
if n<= 0:
    print(" Không hợp lệ. Nhập lại.")
else:
    for i in range( n+ 1):
        S4= S4+ i** 2
        S5= S5+ ( 2* i+ 1)** 3
        S6= S6+ ( 2* i) ** 4
    print(" S4= ", S4)
    print(" S5= ", S5)
    print(" S6= ", S6)
