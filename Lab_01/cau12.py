# Bài 12: Viết chương trình nhập vào vận tốc a của một xe ô tô đang chạy. Khi người lái đạpphanh, tính thời gian ô tô đi được cho đến lúc dừng, biết vận tốc chậm dần đều là 𝑣(𝑡) =−𝑡. log4 5 + 𝑎4 (Làm tròn đến số thập phân thứ hai).

from math import *
a = float(input('Nhập vận tốc ban đầu của ô tô: '))
log4_5 = log(5) / log(4)
t = (a ** 4) / log4_5
print(f'Thời gian ô tô dừng lại: {t:.2f} giây')

