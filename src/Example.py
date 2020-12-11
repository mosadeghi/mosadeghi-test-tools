import generate_output as go
import generate_input as gi
import zipper
import random

TEST_CASES = 100


def input_gen(n):
    inputs = list(map(lambda x: f'{x}', range(1, 101)))
    return inputs


def program(input_lines):
    res = input_lines[0]
    return res


gi.run(input_gen, TEST_CASES)
go.run(program)
zipper.zip()