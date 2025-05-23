def doc_so():
    with open(file='dayso.dat', mode='r') as file:
        numbers = list(map(int, file.readline().strip().split(',')))
        for number in numbers:
            if number % 2 != 0:
                print(number, end=' ')

doc_so()