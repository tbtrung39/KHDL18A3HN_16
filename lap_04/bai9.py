char = input ("nhập một kí tự :")
if len(char) != 1:
    print("vui lòng nhập đúng một ký tự ")
else:
  ascii_code = ord(char)
print( "mã ASCII của kí tự ",char, "là", ascii_code)