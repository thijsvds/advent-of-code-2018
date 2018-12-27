import operator

data = ''
with open('input_day4.txt', 'r') as myfile:
  data = myfile.read()

data_split = data.split('\n')

def clean_line(line):
    d = {}
    c_l = line.strip('[').split(']')
    d['time'] = c_l[0]
    d['minute'] = int(d['time'].split(' ')[1][3:])
    d['action'] = c_l[1][1:]
    return d

def recognize_guard(action):
    return action['action'].split(' ')[1].strip('#')

actions = []

for line in data_split:
    actions.append(clean_line(line))

actions = sorted(actions, key=lambda k: k['time'])

guards = {}
current_guard = ''
fall_asleep = 0
wake_up = 0

for action in actions:
    action_l = action['action'][0]
    
    if action_l == 'G':
        current_guard = recognize_guard(action)
        if guards.get(current_guard) == None:
            guards[current_guard] = [0 for i in range(60)]
    elif action_l == 'f':
        fall_asleep = action['minute']
    elif action_l == 'w':
        wake_up = action['minute']
        for minute in range(fall_asleep, wake_up):
            guards.get(current_guard)[minute] += 1

guards = sorted(guards.items(), key=lambda kv: max(kv[1]))
print(guards)
for guard in guards:
    print(guard[0], max(guard[1]), guard[1].index(max(guard[1])))