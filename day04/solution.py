import unittest
import re
from util import read_file

INPUT = read_file('input.txt')


def get_passports(batch_file):
    data = batch_file.split('\n\n')
    passports = []

    for value in data:
        passports.append(get_passport_dict(value))

    return passports


def get_passport_dict(passport):
    values = {}
    for i in passport.split(' '):
        for j in i.split('\n'):
            key, value = j.split(':')
            values[key] = value
    return values


def validate_passport(passport: dict):
    keys = passport.keys()
    if len(keys) == 8:
        return True
    elif len(keys) == 7 and 'cid' not in keys:
        return True

    return False


def __range_check(value, low, high):
    try:
        year = int(value)
        return low <= year <= high
    except ValueError:
        return False


def dob_check(value):
    return __range_check(value, 1920, 2002)


def issue_check(value):
    return __range_check(value, 2010, 2020)


def expiration_check(value):
    return __range_check(value, 2020, 2030)


def height_check(value: str):
    height = "".join([char for char in value if char.isdigit()])
    unit = "".join([char for char in value if char.isalpha()])
    return (unit == "cm" and __range_check(height, 150, 193)) or (unit == "in" and __range_check(height, 59, 76))


def hair_color_check(value):
    return re.compile(r'#[0-9a-f]{6}').match(value) is not None


def eye_color_check(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def pid_check(value):
    return re.compile(r'\d{9}$').match(value) is not None


def deep_validation(passport: dict):
    if not validate_passport(passport):
        return False

    checks = []

    for key, value in passport.items():
        if key == 'byr':
            checks.append(dob_check(value))
        elif key == 'iyr':
            checks.append(issue_check(value))
        elif key == 'eyr':
            checks.append(expiration_check(value))
        elif key == 'hgt':
            checks.append(height_check(value))
        elif key == 'hcl':
            checks.append(hair_color_check(value))
        elif key == 'ecl':
            checks.append(eye_color_check(value))
        elif key == 'pid':
            checks.append(pid_check(value))
        elif key == 'cid':
            checks.append(True)

    return all(checks)


def part_one(_input):
    passports = get_passports(_input)
    return len([passport for passport in passports if validate_passport(passport)])


def part_two(_input):
    passports = get_passports(_input)
    return len([passport for passport in passports if deep_validation(passport)])


class Day4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_input = read_file('test_input.txt')

    def test_part_one(self):
        self.assertEqual(part_one(self.test_input), 2)

    def test_part_two(self):
        self.assertEqual(part_two(self.test_input), 2)


print(part_one(INPUT))
print(part_two(INPUT))
