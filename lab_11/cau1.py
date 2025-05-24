def read_data_from_file(path):
    with open(path,'r') as file:
        n=int(file.readline().strip())
        