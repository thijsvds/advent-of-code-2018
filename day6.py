data = ''
with open('testinput_day6.txt', 'r') as myfile:
  data = myfile.read()

data_split = data.split('\n')

# Convert text file into coordinates
def read_coordinates(data):
  list_of_coordinates = []
  for line in data:
    x = int(line.split(',')[0])
    y = int(line.split(',')[1].replace(' ', ''))
    list_of_coordinates.append([x, y])
  return list_of_coordinates

# Read the highest values from a list of coordinates
def max_xy(list_of_coords):
  max_x = max([x[0] for x in list_of_coords])
  max_y = max([x[1] for x in list_of_coords])
  return [max_x, max_y]

def create_matrix(max_xy):
  max_x = max_xy[0]
  max_y = max_xy[1]
  return [['' for y in range(0, max_x + 1)] for x in range(0, max_y + 1)]

def plot_coordinates(matrix, coord, name):
  matrix[coord[0]][coord[1]] = name
  return matrix

def circle_around(coordinate, distance):
  min_x = coordinate[0] - distance
  max_x = coordinate[0] + distance
  min_y = coordinate[1] - distance
  max_y = coordinate[1] + distance


def find_closest_location(coordinate):
  x = coordinate[0]
  y = coordinate[y]
  count = 1
  nothing_found = True
  while nothing_found:

  print(coordinates, get_content(coordinates))

def get_content(coordinates):
  return matrix[coordinate[0]][coordinate[1]]

list_of_coordinates = read_coordinates(data_split)

matrix = create_matrix(max_xy(list_of_coordinates))
print(len(matrix))
print(len(matrix[0]))

count = 0
for coord in list_of_coordinates:
  matrix = plot_coordinates(matrix, coord, count)
  count += 1

rowcount = 0
for row in matrix:
  cellcount = 0
  for cell in row:
    find_closest_location([rowcount, cellcount])
    cellcount += 1
  rowcount += 1


