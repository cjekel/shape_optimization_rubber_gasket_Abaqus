from __future__ import print_function
import numpy as np
import pandas as pd
import os
import dlib

def new_mesh_run_model(x):
    # set the state of the jobs
    success = False
    # modify the pre process template file
    with open('write_inp_template.py', 'r') as d, open('write_inp.py', 'w') as f:
        # load the template
        data = d.read()
        # replace the two beta values with the x value
        data = data.replace('BETA1VALUE',str(x[0]))
        data = data.replace('BETA2VALUE',str(x[1]))
        # write the input file
        f.write(data)
    # run the prepprocess file
    val = os.system('abaqus cae noGUI=write_inp.py')
    print(val)
    if val ==0:
        # the mesh was a success
        # execute the job
        val = os.system('abq2018 job=Job-1 interactive cpus=4 ask_delete=OFF > /dev/null')
        # interactive means abaqus waits for the job to finish
        # > /dev/null sends the print out to a non existant drive in order to
        # keep a clean log file
        print(val)

        # read the last line of the job stats fileName
        try:
            with open('Job-1.sta','r') as f:
                read_data = f.readlines()
                print(read_data[-1])
            if read_data[-1] == ' THE ANALYSIS HAS COMPLETED SUCCESSFULLY\n':
                # the analysis was completed successfully
                success = True
        except:
            success = False
    if success== True:
        # execute post process
        return True
    else:
        return False

def post_process(x):
    # run the post_process script
    val = os.system('abaqus cae noGUI=write_res.py')
    print(val)
    # if the script was okay
    if val == 0:
        # calc the average node location for nodes on d1
        d1 = pd.read_csv('d1.csv')
        d1u = np.array(d1.values[:,-1])
        d1x = np.array(d1.values[:,-7])
        d1res = np.mean(d1x+d1u)
        # calc the average node location for nodes on d2
        d2 = pd.read_csv('d2.csv')
        d2u = np.array(d2.values[:,-1])
        d2x = np.array(d2.values[:,-7])
        d2res = np.mean(d2x+d2u)
        # d is the difference between d1 and d2
        d = d2res - d1res # from initial = 0.010154547785833336

        # compute the standard deviation of the contact pressure
        contact_pressure = pd.read_csv('contact_pressure.csv')
        p = contact_pressure.values[:,-1]
        # ignore zero contact pressure surface elements
        p[p==0.0]=np.nan
        p = p.astype(np.float)
        pstd = np.nanstd(p) # from initial = 5188183.430865008
        print('var:', x)
        print('obj:',d,pstd)
        return (d / 0.010154547785833336) + (pstd /8341533.54401)
    else:
        # if the job wasn't succesful return inf
        return np.inf

def my_obj_fun(x0,x1):
    x = [x0,x1]
    # run the pre processing script
    success = new_mesh_run_model(x)
    if success == True:
        # run the post processing script
        obj = post_process(x)
    else:
        obj = np.inf
    return obj

# run optimization using Lipschitz functions
x,y = dlib.find_min_global(my_obj_fun,[0.003,0.003],[0.035,0.035],10)

print('******** OPT FOUND *******')
print('X:', x)
print('Y:', y)
