from sys import argv
from matrix_generation import generate_first_step_matrix, generate_n_step_matrix

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

# Extract data from input
empty_map_file = "victoria_lake/empty_map.txt"
empty_map_string = ''
contents_of_file = open(empty_map_file, 'w')
for index, line in enumerate(input_file_contents.split('\n')):
    # First line
    if index == 0:
        map_info = line.split(' ')
        map_info = map(int, map_info)
        width, height, number_of_customers, available_offices = map_info
    # Coordinates and value of customers
    elif 0 < index <= number_of_customers:
        map_info = line.split(' ')
        map_info = list(map(int, map_info))
        customers_data[(map_info[0], map_info[1])] = map_info[2]
    # Map itself
    else:
        if line == '':
            pass
        else:
            empty_map_string += f"{line}\n"
contents_of_file.write(empty_map_string)
contents_of_file.close()

print(f'this are the customers: {customers_data}')

customer_matrices = []

# Cover map with calculations of depth 1 for each customer
for coordinates, value in customers_data.items():
    storage_file = generate_first_step_matrix(empty_map_file, coordinates, value)
    customer_matrices.append(storage_file)

# Cover map with calculations of depth n-1 for each customer
for customer_matrice in customer_matrices:
    generate_n_step_matrix(customer_matrice, height-1)

print(customer_matrices)