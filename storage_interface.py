from re import sub

def save_map_as_txt_file(map_as_list, customer_coordinates):
    filename = f"victoria_lake/{customer_coordinates}.txt"
    contents_of_file = open(filename, 'w')
    text = ''
    for line in map_as_list:
        for element in line:
            text += f'{element}, '
        text += '\n'
    text = sub(", \n", "\n", text)
    contents_of_file.write(text)
    contents_of_file.close()
    return filename

def get_map_as_list(filename):
    contents_of_file = open(filename, 'r').read()
    map_as_list = []
    for line in contents_of_file.split('\n'):
        line_list = []
        for charachter in line:
            line_list.append(charachter)
        map_as_list.append(line_list)
    return map_as_list

def get_map_with_elements_separated_by_commas_as_list(filename):
    contents_of_file = open(filename, 'r').read()
    map_as_list = []
    for line in contents_of_file.split('\n'):
        line_list = []
        for charachter in line.split(', '):
            line_list.append(charachter)
        if line_list != ['']:
            map_as_list.append(line_list)
    return map_as_list
