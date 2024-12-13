from contextlib import contextmanager

@contextmanager
def open_file (filename, mode):
    file = open (filename, mode)
    yield file
    file.close()

with open_file('sample.txt', 'w') as file:
    file.write ("hello. iam erosha!")

print (file.closed)
