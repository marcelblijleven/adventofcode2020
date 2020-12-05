def read_lines(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return lines


def get_input(file_name):
    lines = read_lines(file_name)
    return [line.strip() for line in lines]


def read_file(file_name):
    with open(file_name) as file:
        content = file.read()

    return content
