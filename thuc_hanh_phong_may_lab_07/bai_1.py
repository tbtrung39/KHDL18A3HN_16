#Bài 1:
import msvcrt

kytu_set = set()

print("Nhập các ký tự (Nhấn phím ESC để kết thúc): ")

while True:
    kytu = msvcrt.getch().decode('utf-8')
    if kytu == '\x1b':
        print("Kết thúc nhập")
        break
    if len(kytu) and kytu.isalpha():
        kytu_set.add(kytu)

print("Kết quả:", kytu_set)