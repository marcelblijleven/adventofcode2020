def get_input(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return [line.strip() for line in lines]
