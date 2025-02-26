# Nhập số nguyên từ người dùng
number = int(input("Nhập một số nguyên có ba chữ số: "))

if not (100 <= number <= 999):
     print("Số không hợp lệ.")

ones = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
tens = ["mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

hundreds_digit = number // 100
tens_digit = (number % 100) // 10
ones_digit = number % 10

result = ones[hundreds_digit] + " trăm "

if tens_digit == 0 and ones_digit == 0:
  print(result.strip()) 
elif tens_digit == 0:
    result += "lẻ " + ones[ones_digit]
elif tens_digit == 1:
    if ones_digit == 0:
      result += "mười"
    else:
      result += "mười " + ones[ones_digit]
else:
    result += tens[tens_digit - 1]
    if ones_digit != 0:
      result += " " + ones[ones_digit]
# In 
print('Cách đọc là:',result)


