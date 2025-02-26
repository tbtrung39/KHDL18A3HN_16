def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    tram = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    if n < 100 or n > 999:
        return "Số nhập vào không hợp lệ! Vui lòng nhập số có ba chữ số."
    t = n // 100
    c = (n % 100) // 10
    d = n % 10
    result = tram[t]
    if c == 0 and d != 0:
        result += " linh " + don_vi[d]
    elif c == 1:
        if d == 0:
            result += " mười"
        elif d == 5:
            result += " mười lăm"
        else:
            result += " mười " + don_vi[d]
    else:
        result += " " + chuc[c]
        if d == 5 and c != 0:
            result += " lăm"
        elif d != 0:
            result += " " + don_vi[d]
    return result.strip()
n = int(input("Nhập vào số nguyên có ba chữ số: "))
print("Cách đọc: ", doc_so(n))