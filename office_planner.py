from sys import argv

script, file_name = argv

input_file = open(file_name)
input_file_contents = input_file.read()

# Variables
cost_of_terrain = {
    '~': 800,
    '*': 200,
    '+': 150,
    'X': 120,
    '_': 100,
    'H': 70,
    'T': 50,
}
width = None
height = None
number_of_customers = None
available_offices = None
customers_data = {}

# Dynamic variables
map_representation = []

# Extract data from input
for index, line in enumerate(input_file_contents.split('\n')):
    if index == 0:
        print(line)
        list_of_data = line.split(' ')
        print(list_of_data)
        width, height, number_of_customers, available_offices = int(list_of_data[0]), int(list_of_data[1]), int(list_of_data[2]), int(list_of_data[3])
    elif 0 < index <= number_of_customers:
        list_of_data = line.split(' ')
        customers_data[(int(list_of_data[0]), int(list_of_data[1]))] = int(list_of_data[2])
    else:
        if line == '':
            pass
        else:
            line_list = []
            for charachter in line:
                line_list.append(charachter)
            map_representation.append(line_list)


print(f'The map width is: {width}, height: {height}, number of customers is {number_of_customers}, and the available offices are: {available_offices}')
print(f'this are the customers: {customers_data}')

# Populate map with customers
for coordinates, value in customers_data.items():
    map_representation[coordinates[1]][coordinates[0]] = value

for line in map_representation:
    print(line)

# Expand from numbered fields in diamond shape
diamond_shape_around_fields = []
current_field_value = None
for y, line in enumerate(map_representation):
    for x, field in enumerate(line):
        if isinstance(field, int):
            current_field_value = field
            # Up
            try:
                diamond_shape_around_fields.append([x, y-1, current_field_value - cost_of_terrain[map_representation[y-1][x]]])
            except:
                pass
            # Right
            try:
                diamond_shape_around_fields.append([x+1, y, current_field_value - cost_of_terrain[map_representation[y][x+1]]])
            except:
                pass
            # Down
            try:
                diamond_shape_around_fields.append([x, y+1, current_field_value - cost_of_terrain[map_representation[y+1][x]]])
            except:
                pass
            # Left
            try:
                diamond_shape_around_fields.append([x-1, y, current_field_value - cost_of_terrain[map_representation[y][x-1]]])
            except:
                pass

for field in diamond_shape_around_fields:
    map_representation[field[1]][field[0]] = field[2]
    
print('---------------------------------------')
print('---------------------------------------')
print('---------------------------------------')
print('---------------------------------------')
print('---------------------------------------')

max_charachters = 0

for line in map_representation:
    if len(str(line)) > max_charachters:
        max_charachters = len(str(line))

for line in map_representation:
    print(line)
print(max_charachters)