import re

from util import get_input

INPUT = get_input('input.txt')
pattern = re.compile(r'(\d+)-(\d+) (\w+): (\w+)')


class PasswordHelper:
    def __init__(self, line):
        matches = re.match(pattern, line).groups()
        self.lower_bound = int(matches[0])
        self.upper_bound = int(matches[1])
        self.letter = matches[2]
        self.password = matches[3]
        self.range = range(self.lower_bound, self.upper_bound + 1)

    def is_valid(self):
        return self.password.count(self.letter) in self.range

    def is_valid_part_two(self):
        position_one = self.password[self.lower_bound - 1] == self.letter
        position_two = self.password[self.upper_bound - 1] == self.letter
        return not position_one == position_two


def part_one(_input):
    passwords = map(PasswordHelper, _input)
    return len([password for password in passwords if password.is_valid()])


def part_two(_input):
    passwords = map(PasswordHelper, _input)
    return len([password for password in passwords if password.is_valid_part_two()])


def test():
    _input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    print(part_two(_input))
    assert part_one(_input) == 2
    assert part_two(_input) == 1


test()
print(part_one(INPUT))
print(part_two(INPUT))
