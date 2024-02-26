# Automate Parsing and Renaming of Multiple Files

import os

working_path = 'A:/python-MyPyCodes/AutomateExample'
os.chdir(working_path)

folder_path = working_path + '/folder'
result_path = working_path + '/result'
os.mkdir(result_path)
for f in os.listdir(folder_path):
    f_name, f_ext = os.path.splitext(f)
    fruit, count, index = f_name.split('-')
    fruit = fruit.strip()
    count = 'cnt' + count.strip().split('_')[1]
    index = index.strip()[1:].zfill(2)
    new_name = '{}-{}-{}{}'.format(index,fruit,count,f_ext)
    new_file = os.path.join(result_path, new_name)
    with open(new_file, 'w') as nf:
        print(new_file)
        pass
