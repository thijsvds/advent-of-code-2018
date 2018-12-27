data = ''
with open('input_day3.txt', 'r') as myfile:
  data = myfile.read()

data_split = data.split('\n')

def clean_line(line):
    d = {}
    line = line.split(' ')
    d['claim'] = int(line[0][1:])
    coords = line[2].strip(':').split(',')
    d['coord_left'] = int(coords[0])
    d['coord_top'] = int(coords[1])
    surface = line[3].split('x')
    d['width'] = int(surface[0])
    d['height'] = int(surface[1])
    return d

the_fabric = [[0 for i in range(1000)] for i in range(1000)]

def claim_in_fabric(claim):
    for row in range(claim['height']):
        for col in range(claim['width']):
            the_fabric[claim['coord_top']+row][claim['coord_left']+col] += 1

for line in data_split:
    claim_in_fabric(clean_line(line))


total_sum = 0
for line in the_fabric:
    for i in line:
        if i > 1:
            total_sum += 1

print(total_sum)

def check_claim_in_fabric(claim):
    for row in range(claim['height']):
        for col in range(claim['width']):
            if the_fabric[claim['coord_top']+row][claim['coord_left']+col] != 1:
                return False
    return True

for line in data_split:
    the_claim = clean_line(line)
    if check_claim_in_fabric(the_claim):
        print(the_claim)
