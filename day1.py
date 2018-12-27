with open('input_day1.txt', 'r') as of:
    nbs = list(map(int, list(map(str.strip, of.readlines()))))
    freqs_reached = set([0])
    freq = 0
    while True:
        for nb in nbs:
            freq += nb
            if freq in freqs_reached:
                print(freq)
                break
            freqs_reached.add(freq)