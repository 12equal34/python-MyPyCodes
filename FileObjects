# File Objects
# : How to read and write to files?

def make_file_bad(file_name):
    'makes a file with some contents.'
    # Open a file with mode: 'r','w','x','a','b','t','+'
    f = open(file_name, 'w+')
    try:
        f.write('1) First line\n')
        f.write('2) Second line\n')
        f.write('3) Third line\n')
        print(f.name)
        print(f.mode)

        print('current pos:', f.tell())
        f.seek(0)
        print('after f.seek(0):', f.tell())
        print(file_name + "'s content is that:")
        print(f.read())
    finally:
        f.close() # If you don't close a file, then resource leak occurs. 
        pass      # But You should use context manager.

make_file_bad('test.txt')

def make_file(file_name):
    'makes a file with some contents.'
    with open(file_name, 'w+') as f: # This is context manager.
        f.write('1) First line\n')
        f.write('2) Second line\n')
        f.write('3) Third line\n')

        print('File name:', f.name)
        print('File mode:', f.mode)

        f.seek(0)
        f_contents = f.read()
        print('File contents:')
        print(f_contents)
    pass

make_file('test2.txt')

def read_file(file_name):
    with open(file_name, 'r') as rf:
        print('method1:')
        total_content = rf.read()
        print(total_content)
        rf.seek(0)

        print('method2:')
        for line in rf.readlines():
            print(line, end='')
        print()
        rf.seek(0)
        
        print('method3:')
        line = rf.readline()
        while len(line) > 0:
            print(line, end='')
            line = rf.readline()
        print()
        rf.seek(0)

        print('method4:')
        for line in rf:
            print(line, end='')
        print()
        rf.seek(0)

        print('method5:')
        size_to_read = 4
        content_read = rf.read(size_to_read)
        while len(content_read) > 0:
            print(content_read, end='*')
            content_read = rf.read(size_to_read)
        print()
        rf.seek(0)

read_file('test2.txt')

def copy_text_file(file_name, copy_file_name):
    size_to_read = 10
    with open(copy_file_name, 'w') as wf:
        with open(file_name, 'r') as rf:
            content = rf.read(size_to_read)
            while len(content) > 0:
                wf.write(content)
                content = rf.read(size_to_read)

copy_text_file('test2.txt', 'copied_test2.txt')

def copy_image_file(file_name, copy_file_name):
    chunk_size = 4096
    with open(copy_file_name, 'wb') as wf:
        with open(file_name, 'rb') as rf:
            chunk = rf.read(chunk_size)
            while len(chunk) > 0:
                wf.write(chunk)
                chunk = rf.read(chunk_size)

copy_image_file('test.jpg', 'copied_test.jpg')