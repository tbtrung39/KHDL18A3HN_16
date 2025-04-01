from collections import defaultdict

sentence = input("Nhập một câu: ").lower().split()
word_count = defaultdict(int)
for word in sentence:
    word_count[word] += 1

print("Số lần xuất hiện của từng từ:")
for word, count in word_count.items():
    print(f"{word}: {count}")