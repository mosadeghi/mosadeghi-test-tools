import random

TEST_CASES = 100

def input_gen(n):
    inputs = list(map(lambda x:f'{x}', range(1,101)))
    return inputs


def program(input_lines):
    res = input_lines[0]
    return res


import generate_input as gi, generate_output as go
gi.run(input_gen, TEST_CASES)
go.run(program)

