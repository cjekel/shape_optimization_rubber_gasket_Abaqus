import os
cwd = os.getcwd()
if os.name == 'nt':
    cwd = os.path.abspath(os.path.expanduser(cwd))
# open the Abaqus replay files
with open('write_inp_template.py','r') as f, open('write_res.py','r') as d:
    write_inp_template = f.readlines()
    write_res = d.readlines()

    # if windows
    write_inp_template[12] = "mydir = '" + cwd + "/'\n"
    write_res[12] = "mydir = '" + cwd + "/'\n"

# save replay files with new current working directory
with open('write_inp_template.py','w') as f, open('write_res.py','w') as d:
    f.write(''.join(write_inp_template))
    d.write(''.join(write_res))
