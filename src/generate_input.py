import os, read_and_write

def list_of_files(dir):
    arr = list(map(lambda x: f"{dir}/{x}",os.listdir(dir)))
    return arr

def run(input_gen, n):
    inputs = []
    lof = list_of_files('./in')
    for inp in lof:
        print(inp)
        inputs.append(''.join(read_and_write.read(inp)))
        
    inputs = inputs + input_gen(n - len(inputs))[0:n - len(inputs)]

    i = 1
    for inputi in inputs:
        read_and_write.write(f"./in/input{i}.txt",inputi)
        i += 1