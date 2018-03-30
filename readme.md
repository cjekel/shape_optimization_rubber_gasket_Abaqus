# About

Design a rubber gasket using shape optimization and Abaqus non-linear finite element solver. For more information read the [report.pdf](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/raw/master/report.pdf). (clicking this link will download report.pdf) Please excuse my typos -- The figures should give you a general idea of what is going on.

# Information

This is working on both Windows and Linux.

I am using the 2018 Abaqus solver with the environment variable name *abq2018*. If you have a different Abaqus solver, change [line 29](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/optimization.py#L29) of optimization.py.

# How it works

We have a parametric design as so:
![Parametric design](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/raw/master/pictures/param.png)

where you are trying to find β0 and β1 that minimize the closure gap and reduces the deviations in the contact pressure. We can use optimization to find the best β0 and β1. I used MaxLIPO algorithm described [here](http://blog.dlib.net/2017/12/a-global-optimization-algorithm-worth.html) that is implemented into the dlib library.

The project is currently set up to use a scipy optimization (Nedler-Mead because of potentially discontinuity) as default. If you want to try out MaxLIPO install the dlib library and uncomment the dlib functions of optimization.py.

The processes required to evaluate the objective function:
1. Open Abaqus sketch and change dimmensions.
2. Generate new mesh.
3. Write Abaqus input file and close Abaqus.
4. Submit Abaqus input file.
5. Verify that Abaqus solver completely succesfully.
6. Run Abaqus post processing script to export distance and contract pressure.
7. Calculate objective function in Python from exported data.

The objective function returns np.inf if any of the above steps fail.  

# File description

| File        | Description  |
| ------------- |-------------|
| [contact_pressure.csv](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/contact_pressure.csv)      | Exported contact pressure of nodes on the surface of the gasket. |
| [d1.csv](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/d1.csv)    | Exported nodal displacement values at one surface of the gasket.    |
[d2.csv](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/d2.csv)    | Exported nodal displacement values at one surface of the gasket.    |
| [opt_struct.cae](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/opt_struct.cae)  | Abaqus cae database file |
| [optimization.py](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/optimization.py) | Python file used to Calculate the objective function and run the optimization. This file is responsible for initiating all of the pre and post processing. |
| [write_current_dir.py](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/write_current_dir.py) | This Python script is used to write the current working directory into the Abaqus replay files used to aid the pre and post processing |
| [write_inp.py](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/write_inp.py) | Abaqus replay file which: 1) Edits sketch. 2) Generates mesh. 3) Write Input file. |
| [write_inp_template.py](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/write_inp_template.py) | Template used to write dimensions to write_inp.py for a particular β0 and β1. |
| [write_res.py](https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus/blob/master/shape_opt/write_res.py) | Abaqus post processing replay file which is used to export nodal displacements and contact pressures. |

All of these files are located in the shape_opt folder.

# How to run

1. Download or clone this library.
```
git clone https://github.com/cjekel/shape_optimization_rubber_gasket_Abaqus.git
```
2. Move into the shape_opt folder.
```
cd shape_opt
```
3. Write the current working directory to the Abaqus replay files.
```
python write_current_dir.py
```
4. Run the optimization.
```
python optimization.py
```
5. Enjoy. :)
