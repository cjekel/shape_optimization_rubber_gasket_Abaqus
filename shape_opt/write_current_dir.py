import os
cwd = os.getcwd()

# open the Abaqus replay files
with open('write_inp_template.py','r') as f, open('write_res.py','r') as d:
    write_inp_template = f.readlines()
    write_res = d.readlines()
    if os.name == 'nt':
        # if windows
        write_inp_template[12] = "mydir = r'" + cwd + "'\n"
        write_res[12] = "mydir = r'" + cwd + "'\n"
    else:
        # if windows
        write_inp_template[12] = "mydir = '" + cwd + "'\n"
        write_res[12] = "mydir = '" + cwd + "'\n"

# save replay files with new current working directory
with open('write_inp_template.py','w') as f, open('write_res.py','w') as d:
    f.write(''.join(write_inp_template))
    d.write(''.join(write_res))
