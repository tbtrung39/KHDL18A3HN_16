bk= float(input("nhập bán kính R vào từ bàn phím: "))
cao= float(input("nhập chiều cao H vào từ bàn phím: "))
dtxq=cao*2*3.14*bk
dttp=dtxq+2*3.14*bk*bk
v=cao*3.14*bk*bk
print("diện tích xung quanh của khối trụ là: %0.2f"%dtxq)
print("diện tích toàn phần của khối trụ là: %0.2f"%dttp)
print("thể tích của khối trụ: là %0.2f"%v)