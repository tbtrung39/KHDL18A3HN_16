n=int(input("NHập số lượng sinh viên: "))
C = set(map(int, input("Danh sách sv thi C++(cách nhau dấu cách): ").split()))
Java = set(map(int, input("Danh sách sv thi Java(cách nhau dấu cách): ").split()))
Python = set(map(int, input("Danh sách sv thi Python(cách nhau dấu cách): ").split()))
sv_thi_3nn = C & Java & Python
sv_thi_2nn = (C & Java) | (C & Python) | (Java & Python)-sv_thi_3nn
sv_thi_1nn = (C | Java | Python) -(sv_thi_3nn|sv_thi_2nn)
print("Sinh viên thi 3 ngôn ngữ: ",sv_thi_3nn)
print("Sinh viên thi 2 ngôn ngữ: ",sv_thi_2nn) 
print("Sinh viên thi 1 ngôn ngữ: ",sv_thi_1nn) 

