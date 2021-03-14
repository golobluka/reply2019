from sys import argv
import os

map_name = "1_victoria_lake.txt"
file_directory = os.path.dirname(__file__)

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

# Tool functions

def print_m(matrix):
    for line in matrix:
        for element in line:
            element = str(element)
            length = len(element)
            print(element + ' ' * (5 - length), end=" ")
        print()

# Extract data from input
with open(os.path.join(file_directory, map_name), "r") as file:
    input_file_contents = file.read()
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


# print(f'The map width is: {width}, height: {height}, number of customers is {number_of_customers}, and the available offices are: {available_offices}')
# print(f'this are the customers: {customers_data}')





# Expand from numbered fields in diamond shape
# diamond_shape_around_fields = []
# current_field_value = None
# for y, line in enumerate(map_representation):
#     for x, field in enumerate(line):
#         if isinstance(field, int):
#             current_field_value = field
#             # Up
#             try:
#                 diamond_shape_around_fields.append([x, y-1, current_field_value - cost_of_terrain[map_representation[y-1][x]]])
#             except:
#                 pass
#             # Right
#             try:
#                 diamond_shape_around_fields.append([x+1, y, current_field_value - cost_of_terrain[map_representation[y][x+1]]])
#             except:
#                 pass
#             # Down
#             try:
#                 diamond_shape_around_fields.append([x, y+1, current_field_value - cost_of_terrain[map_representation[y+1][x]]])
#             except:
#                 pass
#             # Left
#             try:
#                 diamond_shape_around_fields.append([x-1, y, current_field_value - cost_of_terrain[map_representation[y][x-1]]])
#             except:
#                 pass

# for field in diamond_shape_around_fields:
#     map_representation[field[1]][field[0]] = field[2]
    
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')
# print('---------------------------------------')

# max_charachters = 0

# for line in map_representation:
#     if len(str(line)) > max_charachters:
#         max_charachters = len(str(line))

# for line in map_representation:
#     print(line)
# print(max_charachters)

def generate_matrix(map_representation, active):
    #Pomožna funkcija
    def max_value(x, y, biggest_till_now):
        for direction in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            hor = x + direction[1] 
            ver = y + direction[0]
            if 0 <= hor and width > hor and 0 <= ver and ver < height:
                element = map_representation[ver][hor]
                if isinstance(element, int) and element > biggest_till_now:
                    biggest_till_now = element
        return biggest_till_now

    #Glavni del
    new_active = []
    for element in active:
        for direction in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            x = element[0] + direction[0]
            y = element[1] + direction[1]
            if 0 <= x and width > x and 0 <= y and y < height:
                if isinstance((map_representation[y][x]), str) and (map_representation[y][x] != '#'):
                    best_choice = max_value(x, y, element[2])
                    value = best_choice - cost_of_terrain[map_representation[y][x]]
                    map_representation[y][x] = value
                    new_active.append((x, y, value))
    return map_representation, new_active




matrices = {}
for customer in customers_data.keys():
    new_map = []
    for i, column in enumerate(map_representation):
        new_map.append([])
        for j, element in enumerate(column):
            if i == customer[1] and j == customer[0]:
                new_map[-1].append(customers_data[customer])
            else:
                new_map[-1].append(element)
    matrices[customer] = new_map

active = [(10, 19, customers_data[(10, 19)])] 
matrix = matrices[(10, 19)]   


for iteration in range(1, 50):
    matrix, active = generate_matrix(matrix, active)  
print_m(matrix)        
