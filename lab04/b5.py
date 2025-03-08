
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Giá trị nhập vào không hợp lệ. Vui lòng nhập lại n: "))
tong_cac_chu_so = 0  
while n > 0:
    chu_so = n % 10  
    tong_cac_chu_so += chu_so   
    n = n // 10  

print(f"Tổng các chữ số của số nguyên dương vừa nhập là: {tong_cac_chu_so}")