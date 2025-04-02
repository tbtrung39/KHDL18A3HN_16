import random
ds = [so for so in range(201) if so % 5 == 0 and so % 7 == 0]
so_ngau_nhien = random.choice(ds)
print("Số được chọn ngẫu nhiên:", so_ngau_nhien)
