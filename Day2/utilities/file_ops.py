def read(filename):
    with open(filename,'r') as f:
        return f.read()

def write(filename, content):
    with open(filename,'w') as f:
        f.write(content)

def search(filename, keyword):
    with open(filename,'r') as f:
        return any(keyword in line for line in f)
