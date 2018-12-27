data = ''
with open('input_day2.txt', 'r') as myfile:
  data = myfile.read()

data_split = data.split('\n')

def frequency_distribution(line):
    count_letters = {}
    for letter in line:
        if count_letters.get(letter):
            count_letters[letter] += 1
        else:
            count_letters[letter] = 1
    return count_letters

twos = 0
threes = 0

for line in data_split:
    frequency_dist = frequency_distribution(line)
    two = False
    three = False
    for frequency in frequency_dist.values():
        if frequency == 2:
            two = True
        elif frequency == 3:
            three = True
    if two == True:
        twos += 1
    if three == True:
        threes += 1

answer = twos * threes

print(answer)

for line in data_split:
    for other_line in data_split:
        count = 0
        count_pos = 0
        for i in range(len(line)):
            if line[i] != other_line[i]:
                count += 1
                count_pos = i
        if count == 1:
            print(other_line)
            print(line)
            print(i)
    