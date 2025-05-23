def thong_tin_khach_hang(pasenger_file, weight_file, canceled_file):
    with open(file= pasenger_file,
              mode= 'r') as pasenger, open(file= weight_file,
                                                   mode= 'w') as weight, open(file= canceled_file,
                                                                                      mode= 'w') as canceled:

        for i, j in enumerate(pasenger, start= 1):
            parts = j.strip().split()
            pasenger_id = j[0]
            name = j[1]
            flight = j[2]
            bags = int(parts[3])
            weights = list(map(float, parts[4:]))
            total_weight = sum(weights)

            if bags > 5 and total_weight > 23:
                canceled.write(f'{i}')
            else:
                weight.write(f'{pasenger_id}, {total_weight:.1f}')

thong_tin_khach_hang('PASSENGER.IN', 'WEIGHT.OUT', 'CANCELED.OUT')