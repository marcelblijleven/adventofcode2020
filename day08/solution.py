from util import get_input

TEST_INPUT = get_input('test_input.txt')
INPUT = get_input('input.txt')

OPERATION_ACC = 'acc'
OPERATION_JMP = 'jmp'
OPERATION_NOP = 'nop'


def part_one(_input):
	instructions = [parse_instruction(line) for line in _input]
	accumulator = isolation_run(instructions)
	return accumulator


def part_two(_input):
	pass


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
		seen_idxs.append(idx)
		operation, argument = instructions[idx]

		if operation == OPERATION_NOP:
			idx += 1
			continue
		elif operation == OPERATION_ACC:
			accumulator += argument
			idx += 1
		elif operation == OPERATION_JMP:
			idx += argument
		else:
			raise ValueError('unrecognized operation received')

	return accumulator


print(part_one(INPUT))
