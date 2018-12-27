data = ''
with open('input_day6.txt', 'r') as myfile:
  data = myfile.read()

data_split = data.split('\n')

def data_to_coord(line):
  coord_x = int(line.split(',')[0])
  coord_y = int(line.split(',')[1].replace(' ', ''))
  return [coord_x, coord_y]

def data_to_coords(data_file):
  list_of_coords = []
  for data_line in data_file:
    list_of_coords.append(data_to_coord(data_line))
  return list_of_coords

def max_xy(list_of_coords):
  max_x = max([x[0] for x in list_of_coords])
  max_y = max([x[1] for x in list_of_coords])
  return [max_x, max_y]

def create_matrix(max_xy):
  return [['' for y in range(0, max_xy[1]+1)] for x in range(0, max_xy[0]+1)]

def plot_coords(matrix, coord, name):
  matrix[coord[0]][coord[1]] = name
  return matrix

def coords_by_taxi(coord, diff):
  coords_reachable = []
  x = coord[0]
  y = coord[1]
  for i in range(0, diff):
    coords_reachable.append([x + i, y + diff -i])
    coords_reachable.append([x + diff -i, y + i])
    coords_reachable.append([x - i, y - diff -i])
    coords_reachable.append([x - diff -i, y - i])
  return coords_reachable

def get_coord(coord, matrix):
  x = coord[0]
  y = coord[1]
  return matrix[x][y]

def find_closest_place(matrix, coord):
  x = coord[0]
  y = coord[1]
  diff = 1
  closest_place = None
  while closest_place == None:
    for coordi in coords_by_taxi(coord, diff):
      current_loc = get_coord(coordi, matrix)
      if current_loc != '':
        closest_place = current_loc
    diff += 1
  return 'c' + str(closest_place)

list_c = data_to_coords(data_split)
matrix = create_matrix(max_xy(list_c))

count = 0
for coord in list_c:
  matrix = plot_coords(matrix, coord, count)
  count += 1

print(find_closest_place(matrix, [800,0]))

