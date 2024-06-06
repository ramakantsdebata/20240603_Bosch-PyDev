'''
open(filepath, mode)
    Mode (r w(create/truncate)  a;    t b)
    
close()
read()
readline()
readlines()
write()
writelines()
flush()
seek(offset, whence=0, 1, 2)
tell()
truncate()
'with' block
'''

# sb1 = b"Test"
# print(type(sb1), sb1)

with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a file IO demo.\n")

with open('example.txt', 'r') as file:
    contents = file.read()
    print(f"File contents:\n{contents}")

with open('example.txt', 'a') as file:
    file.write("Appending some text.\n")

with open('example.txt', 'r') as file:
    print("\n\nReading line by line")
    for line in file:
        print(line, end='')

with open('example.txt', 'r') as file:
    print("\n\nSeek and Tell")
    file.seek(0)
    print(f"Cursor position: {file.tell()}")
    print(f"First 5 chars: {file.read(5)}")
    print(f"Cursor position after reading 5 chars: {file.tell()}")
