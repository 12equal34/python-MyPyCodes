# Import OS Module.
import os

print(dir(os))

# Save a path
path = '/Users/12equ/source/repos/python-MyPyCodes'
os.chdir(path)

# Where is a current work directory?
print(os.getcwd())

# Change cwd to the path inputed.
os.chdir('/Users/12equ/source/repos/')
print(os.getcwd())

# Go to upper folder of cwd.
os.chdir('..')
print(os.getcwd())

os.chdir('./repos/python-MyPyCodes')
print(os.getcwd())

# Get the list of subfolders of cwd.
print(os.listdir())

# Make a directory(folder) on cwd. It can't make folder with subfolder.
os.mkdir('Folder1')
# os.mkdir('Folder1/SubFolder1') is error.
print(os.listdir())

# Remove a directory(folder) on cwd.
os.rmdir('Folder1')
# os.rmdir('Folder1/SubFolder1') is error.
print(os.listdir())

# Make folders on cwd with subfolders at once if you needs.
os.makedirs('Folder2/SubFolder1')
print(os.listdir())

os.removedirs('Folder2/SubFolder1')
print(os.listdir())

# Create a new file
file_name = 'file1.txt'
with open(file_name, 'w') as f:
    pass
print("After creating a new file:", file_name)
print(os.listdir())
print()

# Rename the file.
new_file_name = file_name + '_changed'
os.rename(file_name, new_file_name)
print("After renaming:", file_name, "to", new_file_name)
print(os.listdir())
print()

# Print the stat of a file.
print("The stat of", new_file_name, "is that")
file_stat = os.stat(new_file_name)
print(file_stat)

from datetime import datetime
modification_time = file_stat.st_mtime
print("the latest time modifying: ", datetime.fromtimestamp(modification_time))
print()

os.remove(new_file_name)
print(os.listdir())

# Get all subdirectories from path by DFS.
exam_path = '/Users/12equ/source/repos/Doodle'
for dirpath, dirnames, filenames in os.walk(exam_path):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
print()

# Get the environment variable.
print('HOME:', os.environ.get('HOME'))
print('PATH:', os.environ.get('PATH'))
print()

# Path join
file_path = os.path.join('C:', path.replace('/', '\\'), 'OSModule.py')
print(file_path)
print()

print('There is a path of', file_path + ':', os.path.exists(file_path))
print('Is a file?:', os.path.isfile(file_path))

# Path names
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print()

