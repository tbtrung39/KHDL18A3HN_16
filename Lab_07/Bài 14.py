tu_dien = {i: bin(i)[2:] for i in range(1, 101)}
print(", ".join([f"({key}, '{value}')" for key, value in tu_dien.items()]))