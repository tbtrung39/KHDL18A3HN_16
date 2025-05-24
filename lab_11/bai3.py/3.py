def ghi_cuc_tri_vao_file(f_input, f_output):
    with open(f_input, 'r') as f:
        numbers = list(map(int, f.read().strip().split()))
    
    cuc_tri = []
    for i in range(1, len(numbers) - 1):
        if (numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]) or \
           (numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]):
            cuc_tri.append(numbers[i])
    
    with open(f_output, 'w') as f:
        f.write(str(len(cuc_tri)) + '\n')
        f.write(' '.join(map(str, cuc_tri)))

# Ví dụ gọi hàm
ghi_cuc_tri_vao_file("f_in.dat", "f_out.dat")