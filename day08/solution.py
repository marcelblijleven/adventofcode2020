from util import get_input, solution_timer

TEST_INPUT = get_input('test_input.txt')
INPUT = get_input('input.txt')

OPERATION_ACC = 'acc'
OPERATION_JMP = 'jmp'
OPERATION_NOP = 'nop'


@solution_timer(8, 1)
def part_one(_input):
    instructions = [parse_instruction(line) for line in _input]
    accumulator = isolation_run(instructions)
    return accumulator


@solution_timer(8, 2)
def part_two(_input):
    instructions = [parse_instruction(line) for line in _input]
    accumulator = correcting_run(instructions)
    return accumulator


def parse_instruction(line):
    parsed = line.split(' ')
    operation = parsed[0]
    argument = int(parsed[1])
    return operation, argument


def isolation_run(instructions):
    accumulator = 0
    idx = 0
    seen_idxs = []

    while idx not in seen_idxs:
        if idx == len(instructions):
            return accumulator, 1

        seen_idxs.append(idx)
        operation, argument = instructions[idx]

        if operation == OPERATION_NOP:
            idx += 1
        elif operation == OPERATION_ACC:
            accumulator += argument
            idx += 1
        elif operation == OPERATION_JMP:
            idx += argument
        else:
            raise ValueError('unrecognized operation received')

    return accumulator, 0


def verify_correction(instructions):
    return len([i for i in instructions if i[0] == OPERATION_JMP and i[1] == 0]) == 0


def correcting_run(instructions):
    for idx, (operation, argument) in enumerate(instructions):
        if operation in [OPERATION_JMP, OPERATION_NOP]:
            if operation == OPERATION_JMP:
                instructions[idx] = OPERATION_NOP, argument
            elif operation == OPERATION_NOP:
                instructions[idx] = OPERATION_JMP, argument
            accumulator, end_code = isolation_run(instructions)

            if end_code == 1:
                return accumulator
            else:
                instructions[idx] = operation, argument


part_one(INPUT)
part_two(INPUT)
