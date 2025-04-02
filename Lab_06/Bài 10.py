import random
numbers = [i for i in range(201) if i % 5 == 0 and i % 7 == 0]
if numbers:
    random_number = random.choice(numbers)
    print(random_number)
else:
    print("Không có số nào chia hết cho cả 5 và 7 trong khoảng này.")