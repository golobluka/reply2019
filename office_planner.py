import os

# Bigining variables

map_name = "2_himalayas.txt"
results_map = "results"
result_name = "result_" + map_name
file_directory = os.path.dirname(__file__)


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
map_representation = []

# Tool functions
def on_map(x,y):
    '''Checks if point lie on the map.'''
    return x >= 0 and x < width and y >= 0 and y < height


def print_m(matrix):
    '''Function for printing matrices.'''
    for line in matrix:
        for element in line:
            element = str(element)
            length = len(element)
            print(element + ' ' * (5 - length), end=" ")
        print()

def generate_matrix(matrix, active):
    '''Function works recursively and generates values around all the active elements. Active elements are just the elements which were generated in previous cycle. '''
    ##Pomožna funkcija
    def max_value(x, y, biggest_till_now):
        for direction in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            hor = x + direction[1] 
            ver = y + direction[0]
            if on_map(hor, ver):
                element = matrix[ver][hor]
                if isinstance(element, int) and element > biggest_till_now:
                    biggest_till_now = element
        return biggest_till_now

    ##Glavni del
    new_active = []
    for element in active:
        for direction in [(1,0), (0, 1), (-1, 0), (0, -1)]:
            x = element[0] + direction[0]
            y = element[1] + direction[1]
            if on_map(x, y):
                if isinstance((matrix[y][x]), str) and (matrix[y][x] != '#'):
                    best_choice = max_value(x, y, element[2])
                    value = best_choice - cost_of_terrain[matrix[y][x]]
                    matrix[y][x] = value
                    new_active.append((x, y, value))
    return matrix, new_active

def generate_paths(place):
    ''' Takes coordinates of office and generates a path (string) to every profitable costumer. It returns list of all those paths.'''
    ##Auxiliary functions
    def follow_trace(customer, end):
        '''Builds trace from end till end reaches customer.'''
        trace = ""
        while end != customer:
            matrix = matrices[customer]
            possibilities = []
            for direction in [(1,0, "R"), (0, 1, "D"), (-1, 0, "L"), (0, -1, "U")]:
                x = end[0] + direction[0]
                y = end[1] + direction[1]
                value = matrix[y][x]
                if on_map(x, y) and isinstance(value, int):    
                    possibilities.append((x, y, direction[2], value))
            possibilities.sort(key=lambda x: x[3], reverse=True)

            best_choice = possibilities[0]
            trace = trace + best_choice[2]
            end = (best_choice[0], best_choice[1])
        
        return trace
       
    ##Main
    list_of_paths = []
    for customer in customers_data.keys():
        if isinstance(matrices[customer][place[1]][place[0]], int):
            if matrices[customer][place[1]][place[0]] > 0:
                trace = follow_trace(customer, place)
                list_of_paths.append(trace)
    return list_of_paths



# Extract data from input.

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



# Prepearing matrices for every customer. 

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

# Generating matrices.
print("Starting to generate customer matrices.")

for customer in customers_data.keys():
    active = [(customer[0], customer[1], customers_data[customer])] 
    matrix = matrices[customer]   

    while active != []:
        matrix, active = generate_matrix(matrix, active)  


# Summing the resoults of all customer matrices.
sum_matrix = []
positive_sum_matrix = []

for row in range(height):
    sum_matrix.append([0 for counter in range(width)])
    positive_sum_matrix.append([0 for counter in range(width)])
    for column in range(width):
        if map_representation[row][column] == "#":
            sum_matrix[row][column] = "#"
            positive_sum_matrix[row][column] = "#"
        else:
            for customer in matrices.keys():
                element = matrices[customer][row][column]

                if isinstance(element, int):
                    sum_matrix[row][column] += element
                    if element > 0:
                        positive_sum_matrix[row][column] += element


#Finding optimal spots.

best_places = [None for counter in range(available_offices)]
customers = [customer for customers in customers_data.keys()]

for row in range(height):
    for column in range(width):
        if (row, column) in customers:
            pass
        else:
            element = positive_sum_matrix[row][column]
            if isinstance(element, int):
                for i, member in enumerate(best_places):
                    if member == None or member[2] < element:
                        best_places[i] = (column, row, element)
                        break
                    else:
                        pass


# Generateing paths to customers.
print("Starting to generate paths to costumers.")

path_dictionary = {}
for place in best_places: 
    list_of_paths = generate_paths(place)
    path_dictionary[place] = list_of_paths


# Write output text file.

with open(os.path.join(file_directory, results_map, result_name), "w") as file:
    for office in path_dictionary.keys():
        for path in path_dictionary[office]:
            text = str(office[0]) + " " + str(office[1]) + " " + path + "\n"
            file.write(text)



