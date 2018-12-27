import string

data = ''
with open('input_day5.txt', 'r') as myfile:
  data = myfile.read()

def one_lower_letter(string):
    if sum(1 for c in string if c.islower()) == 1:
        return True
    return False

def same_letter(string):
    if string[0].lower() == string[1].lower():
        return True
    return False

def react_string(string):
    return_string = string
    global start_i
    for i in range(start_i, len(string)-1):
        to_check = string[i:i+2]
        if one_lower_letter(to_check) and same_letter(to_check):
            
            start_i = max(i-1, 0)
            return string.replace(to_check, '', 1)
    return return_string

lengths = []

for l in string.ascii_lowercase:
    start_i = 0
    count = 0
    data2 = data.replace(l, '')
    data2 = data2.replace(l.upper(), '')
    while len(react_string(data2)) < len(data2):
        data2 = react_string(data2)
    count += 1
    lengths.append(len(data2))
    print(l, l.upper(), len(data2))