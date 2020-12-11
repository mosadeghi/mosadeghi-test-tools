import os
import read_and_write


def list_of_files(dir):
    arr = list(map(lambda x: f"{dir}/{x}", os.listdir(dir)))
    return arr


def run(input_gen, n):
    inputs = []
    dictionary = {}

    for inp in list_of_files('./in'):
        number = int(inp.split('input')[1].split('.')[0])-1
        dictionary[number] = ''.join(read_and_write.read(inp))

    for i in range(len(dictionary)):
        inputs.append(dictionary[i])

    if len(inputs) < n:
        inputs = inputs + input_gen(n - len(inputs))[0:n - len(inputs)]

    i = 1
    for inputi in inputs:
        read_and_write.write(f"./in/input{i}.txt", inputi)
        i += 1
