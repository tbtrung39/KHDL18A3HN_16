def tinh_tong_so_le(day_so):
    with open(day_so, 'r') as f:
        numbers = []
        for line in f:
            numbers += map(int, line.strip().split())
    
    tong_le = sum(x for x in numbers if x % 2 == 1)
    return tong_le

print(tinh_tong_so_le("day_so.dat"))
