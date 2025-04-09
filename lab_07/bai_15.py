import random

list1 = [random.randint(1, 100) for i in range(100)]

list2 = ['q','w','e','r','t',
         'y','u','i','o','p',
         'a','s','d','f','g',
         'h','j','k','l','z',
         'x','c','v','b','n','m']

D = dict(zip(list1, list2))

print(D)