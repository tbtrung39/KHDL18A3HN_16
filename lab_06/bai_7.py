List = [["mon", 73],
        ["tue", 89],
        ["wed", 95],
        ["thu", 103],
        ["fri", 115],
        ["sat", 128],
        ["sun", 120]]

List_ = List
print(List_)

print(List[2][1])

list_test = List
print(len(list_test))
import random
list_test.insert(7, ["random", random.randint(1, 999)])
print(list_test)

mon_sale = List[0][1]
tue_sale = List[1][1]
sat_sale = List[-2][1]
sun_sale = List[-1][1]
black_friday = mon_sale + tue_sale + sat_sale + sun_sale
print(black_friday)