# Bài 7: Gộp số chung từ 2 file

def read_numbers(filename):
    with open(filename, 'r') as f:
        return set(map(int, f.read().split()))

def write_common_numbers(m_file, n_file, out_file):
    nums_m = read_numbers(m_file)
    nums_n = read_numbers(n_file)
    common = sorted(nums_m & nums_n)  # giao nhau
    with open(out_file, 'w') as f:
        f.write(' '.join(map(str, common)))

# Gọi hàm
write_common_numbers('m_nums.txt', 'n_num.txt', 'so_chung.txt')
