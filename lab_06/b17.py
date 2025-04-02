sentence = input("Nhập một câu: ").lower().split()
word_count = {}
for word in sentence:
    word_count[word] = word_count.get(word, 0) + 1

print("Số lần xuất hiện của từng từ:")
for word, count in word_count.items():
    print(f"{word}: {count}")
