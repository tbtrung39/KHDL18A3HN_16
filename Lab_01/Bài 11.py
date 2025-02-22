n= int( input(" Nhập số lần tung xúc sắc: "))
prob_all_six = ( 1 / 6) ** 3
print(" Xác suất để cả 3 xúc sắc đều ra 6 trong một lần tung: ", prob_all_six)
prob_no_all_six = (1 - prob_all_six) ** n
print(" Xác suất không có lần nào cả 3 xúc sắc ra 6 trong n lần: ", prob_no_all_six)
prob_at_least_one_all_six = 1 - prob_no_all_six
print(" Xác suất có ít nhất một lần cả 3 xúc sắc ra 6 trong n lần: ", round(prob_at_least_one_all_six, 2))