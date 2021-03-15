def find_neighbour_elements(coordinates, map_as_list):
    x, y = coordinates
    neighbours = []
    try:
        neighbours.append([x, y-1, map_as_list[y-1][x]])
    except:
        pass
    # Right
    try:
        neighbours.append([x+1, y, map_as_list[y][x+1]])
    except:
        pass
    # Down
    try:
        neighbours.append([x, y+1, map_as_list[y+1][x]])
    except:
        pass
    # Left
    try:
        neighbours.append([x-1, y, map_as_list[y][x-1]])
    except:
        pass
    return neighbours

def find_all_integer_elements(map_as_list):
    integer_elemets = []
    for y, line in enumerate(map_as_list):
        for x, element in enumerate(line):
            try:
                integer = (x, y, int(element))
                integer_elemets.append(integer)
            except:
                pass
    return integer_elemets

def find_all_integer_elements_with_non_integer_neighbours(map_as_list):
    integer_elements = find_all_integer_elements(map_as_list)
    integer_elements_with_non_integer_neighbours = []
    for element in integer_elements:
        string_neighbour = False
        coordinates = (element[0], element[1])
        neighbours = find_neighbour_elements(coordinates, map_as_list)
        for neighbour in neighbours:
            try:
                int(neighbour[2])
            except:
                string_neighbour = True
        if string_neighbour:
            integer_elements_with_non_integer_neighbours.append(element)
    return integer_elements_with_non_integer_neighbours