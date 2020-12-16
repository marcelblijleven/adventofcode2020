from unittest import TestCase
from day08.solution import (
    parse_instruction, correcting_run, isolation_run,
    verify_correction, TEST_INPUT
)


class TestParseInstruction(TestCase):
    def test_parse_instruction_nop(self):
        operation, argument = parse_instruction('nop +0')
        self.assertEqual('nop', operation)
        self.assertEqual(0, argument)

    def test_parse_instruction_acc_pos(self):
        operation, argument = parse_instruction('acc +1')
        self.assertEqual('acc', operation)
        self.assertEqual(1, argument)

    def test_parse_instruction_acc_neg(self):
        operation, argument = parse_instruction('acc -1')
        self.assertEqual('acc', operation)
        self.assertEqual(-1, argument)

    def test_parse_instruction_jmp_pos(self):
        operation, argument = parse_instruction('jmp +1')
        self.assertEqual('jmp', operation)
        self.assertEqual(1, argument)

    def test_parse_instruction_jmp_neg(self):
        operation, argument = parse_instruction('jmp -1')
        self.assertEqual('jmp', operation)
        self.assertEqual(-1, argument)

    def test_parse_instruction_double_digit_neg(self):
        operation, argument = parse_instruction('jmp -99')
        self.assertEqual('jmp', operation)
        self.assertEqual(-99, argument)


class TestIsolationRun(TestCase):
    def test_isolation_run(self):
        instructions = [parse_instruction(line) for line in TEST_INPUT]
        accumulator, _ = isolation_run(instructions)
        self.assertEqual(5, accumulator)


class TestVerifyCorrection(TestCase):
    def test_verify_correction(self):
        instructions = [
            ('jmp', 1),
            ('jmp', -1)
        ]

        self.assertTrue(verify_correction(instructions))

    def test_verify_correction_incorrect(self):
        instructions = [
            ('jmp', 0),
            ('jmp', -1)
        ]

        self.assertFalse(verify_correction(instructions))


class TestCorrectingRun(TestCase):
    def test_correcting_run(self):
        instructions = [parse_instruction(line) for line in TEST_INPUT]
        accumulator = correcting_run(instructions)
        self.assertEqual(8, accumulator)
