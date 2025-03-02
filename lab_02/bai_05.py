months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
month = int(input("Nhập vào một tháng (1-12): "))
if 1 <= month <= 12:
    print("Tháng không hợp lệ, vui lòng nhập lại!")
else:
    print(f"Tháng {month} có tên là {months[month - 1]}")
