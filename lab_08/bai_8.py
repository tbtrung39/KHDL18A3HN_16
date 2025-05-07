import math
def perimeter(r):
    return round(2 * math.pi * r, 2)

def acreage(r):
    return round(math.pi * r**2, 2)

r = int(input("Nhập bán kính: "))
print(f'Chu vi và diện tích của bán kính r là: {perimeter(r)} và {acreage(r)}')