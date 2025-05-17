def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def tim_nguyen_to_khac_nhau(f_in, f_out):
    primes = set()
    with open(f_in, 'r') as f:
        for line in f:
            for x in map(int, line.strip().split()):
                if is_prime(x):
                    primes.add(x)
    
    with open(f_out, 'w') as f:
        f.write(str(len(primes)) + '\n')
        f.write(' '.join(map(str, sorted(primes))))

# Gọi hàm
tim_nguyen_to_khac_nhau("f_in.dat", "f_out.dat")
