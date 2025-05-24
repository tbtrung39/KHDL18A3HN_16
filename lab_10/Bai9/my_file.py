def doc_file(ten_file):
    with open(ten_file, 'r', encoding='utf-8') as f:
        return f.read()

def ghi_file(ten_file, noi_dung):
    with open(ten_file, 'w', encoding='utf-8') as f:
        f.write(noi_dung)
