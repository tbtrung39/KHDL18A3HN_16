import random
import math

def tao_day_so():
    return random.sample(range(100), 10)

def chia_het_cho_7(day):
    return [x for x in day if x % 7 == 0]

def tong_day(day):
    return sum(day)

def co_so_chinh_phuong(day):
    return any(int(math.sqrt(x))**2 == x for x in day)
