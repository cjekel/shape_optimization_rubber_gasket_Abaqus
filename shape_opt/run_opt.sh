# warning
# set up write_inp_template.py and write_res.py 
# with current working directory
# I could add this in Python...
time python optimization.py 2>&1 | tee optimization_output.txt
cp optimization_output.txt ~/Dropbox/phdWork/courseWork/2018Spring/EGM6352AdvanceFEA/HW/Project1/
