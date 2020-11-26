import os, re
import read_and_write

def list_of_files(dir):
    arr = list(map(lambda x: f"{dir}/{x}",os.listdir(dir)))
    return arr

def generate_output(program, input_file_name):
    input_lines = read_and_write.read(input_file_name)
    output_name = f"output{input_file_name.split('input')[1].split('.')[0]}.txt"
    read_and_write.write(f"./out/{output_name}",program(input_lines))

def run(program):        
    inps = list_of_files('./in')
    for inp in inps:
        generate_output(program,inp)