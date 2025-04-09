m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
chu_so_m = set(str(m))  
chu_so_n = set(str(n))
chu_so_chung = chu_so_m & chu_so_n
tong = sum(map(int, chu_so_chung))
print("Các chữ số chung là:", " ".join(sorted(chu_so_chung)))
print("Tổng các chữ số chung:", tong)
