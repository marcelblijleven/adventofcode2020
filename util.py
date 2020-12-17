import time


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


def solution_timer(day, part):
    if day is None or part is None:
        raise ValueError('incorrect values provided for solution timer')

    identifier = f'day {day} part {part}'

    def decorator(func):
        def wrapper(*a, **kw):
            try:
                start = time.perf_counter()
                solution = func(*a, **kw)
                diff = (time.perf_counter() - start) * 1000
                print(f'{identifier}: {solution} in {diff:.4f} ms')
            except Exception as e:
                print(e)
            else:
                return solution
        return wrapper
    return decorator
