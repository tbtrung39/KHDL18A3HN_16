import random

# Tạo list số chia hết cho 5 và 7 từ 0 đến 200
valid_numbers = [x for x in range(0, 201) if x % 5 == 0 and x % 7 == 0]

# Chọn ngẫu nhiên 1 số từ list
random_number = random.choice(valid_numbers)
print("Số ngẫu nhiên chia hết cho 5 và 7:", random_number)