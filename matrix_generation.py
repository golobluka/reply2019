from storage_interface import save_map_as_txt_file, get_map_as_list, get_map_with_elements_separated_by_commas_as_list
from helper_methods import find_neighbour_elements, find_all_integer_elements, find_all_integer_elements_with_non_integer_neighbours

cost_of_terrain = {
    '~': 800,
    '*': 200,
    '+': 150,
    'X': 120,
    '_': 100,
    'H': 70,
    'T': 50,
}

def stage_a_change_for_fields_around_element(matrix, element_coordinates, element_value):
    x, y = element_coordinates
    fields_and_their_values = []
    current_field_value = element_value
    # Up
    try:
        fields_and_their_values.append([x, y-1, current_field_value - cost_of_terrain[matrix[y-1][x]]])
    except:
        pass
    # Right
    try:
        fields_and_their_values.append([x+1, y, current_field_value - cost_of_terrain[matrix[y][x+1]]])
    except:
        pass
    # Down
    try:
        fields_and_their_values.append([x, y+1, current_field_value - cost_of_terrain[matrix[y+1][x]]])
    except:
        pass
    # Left
    try:
        fields_and_their_values.append([x-1, y, current_field_value - cost_of_terrain[matrix[y][x-1]]])
    except:
        pass
    return fields_and_their_values

def generate_first_step_matrix(empty_map_file, customer_coordinates, customer_value):
    map_as_list = get_map_as_list(empty_map_file)

    x, y = customer_coordinates
    map_as_list[y][x] = customer_value

    staged_change = stage_a_change_for_fields_around_element(map_as_list, customer_coordinates, customer_value)
    for change in staged_change:
        x, y, value = change
        map_as_list[y][x] = value

    name_of_file = save_map_as_txt_file(map_as_list, customer_coordinates)

    return name_of_file

def generate_n_step_matrix(map_file, depth):
    map_as_list = get_map_with_elements_separated_by_commas_as_list(map_file)
    # kolikor je depth ponovi kodo:
    
    # for round in range(depth):
    # za vsak element v integer_elements preveri ali ima neštevilskega soseda
    integer_elements_with_non_int_neighbours = find_all_integer_elements_with_non_integer_neighbours(map_as_list)
    print(integer_elements_with_non_int_neighbours)
    # najdi vse elemente, integerje, ki mejijo (levo desno gor dol) na ne-integer
    # za vsak element izračunaj vrednosti za polja, ki so mu sosednja
    # vse skupaj zberi v obliki (x, y, načrtovana vrednost elementa)
    # če so kje koordinate iste (torej da je element isti), a je več elementov, izbriši vse razen tistega, katerega vrednost je največja
    # zdaj imaš seznam elementov, ki se morajo spremeniti, brez podvojenih elementov
    # spremeni podobo mape