def write(file_name, content):
    file = open(file_name, mode='w', encoding='utf8')
    file.write(content)
    file.close()

def read(file_name):
    file = open(file_name, mode='r', encoding='utf8')
    lines = file.readlines()
    file.close()
    return lines
