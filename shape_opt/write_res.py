# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2018 replay file
# Internal Version: 2017_11_07-12.21.41 127140
# Run by cj on Wed Mar 21 16:27:40 2018
#
# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
import os
from abaqus import *
from abaqusConstants import *
mydir = '/home/cj/Documents/shape_optimization_rubber_gasket_Abaqus/shape_opt'
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=273.84375,
    height=207.680557250977)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
openMdb(
    pathName=os.path.abspath(mydir+'/opt_struct.cae'))
#: The model database "/home/cj/Dropbox/phdWork/courseWork/2018Spring/EGM6352AdvanceFEA/HW/Project1/abaqus_work/opt_struct.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name=os.path.abspath(mydir+'/Job-1.odb'))
#: Model: /home/cj/Dropbox/phdWork/courseWork/2018Spring/EGM6352AdvanceFEA/HW/Project1/abaqus_work/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       9
#: Number of Node Sets:          12
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs[os.path.abspath(mydir+'/Job-1.odb')])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
odb = session.odbs[os.path.abspath(mydir+'/Job-1.odb')]
session.fieldReportOptions.setValues(reportFormat=COMMA_SEPARATED_VALUES)
session.writeFieldReport(fileName='contact_pressure.csv', append=OFF,
    sortItem='Element Label', odb=odb, step=0, frame=20,
    outputPosition=ELEMENT_NODAL, variable=(('CPRESS', ELEMENT_NODAL), ))
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs[os.path.abspath(mydir+'/Job-1.odb')])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
leaf = dgo.LeafFromNodeSets(nodeSets=(" ALL NODES", ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromNodeSets(nodeSets=(" ALL NODES", ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromNodeSets(nodeSets=("PART-1-1.D1", ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.add(leaf=leaf)
dg = session.viewports['Viewport: 1'].odbDisplay.displayGroup
dg = session.DisplayGroup(name='d1', objectToCopy=dg)
session.viewports['Viewport: 1'].odbDisplay.setValues(visibleDisplayGroups=(dg,
    ))
session.viewports['Viewport: 1'].odbDisplay.displayGroupInstances['d1'].setValues(
    lockOptions=OFF)
session.fieldReportOptions.setValues(reportFormat=COMMA_SEPARATED_VALUES)
session.writeFieldReport(fileName='d1.csv', append=OFF, sortItem='Node Label',
    odb=odb, step=0, frame=20, outputPosition=NODAL, variable=(('U', NODAL, ((
    COMPONENT, 'U1'), )), ))
leaf = dgo.LeafFromNodeSets(nodeSets=(" ALL NODES", ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromNodeSets(nodeSets=(" ALL NODES", ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromNodeSets(nodeSets=("PART-1-1.D2", ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.add(leaf=leaf)
dg = session.viewports['Viewport: 1'].odbDisplay.displayGroup
dg = session.DisplayGroup(name='d2', objectToCopy=dg)
session.viewports['Viewport: 1'].odbDisplay.setValues(visibleDisplayGroups=(dg,
    ))
session.viewports['Viewport: 1'].odbDisplay.displayGroupInstances['d2'].setValues(
    lockOptions=OFF)
session.fieldReportOptions.setValues(reportFormat=COMMA_SEPARATED_VALUES)
session.writeFieldReport(fileName='d2.csv', append=OFF, sortItem='Node Label',
    odb=odb, step=0, frame=20, outputPosition=NODAL, variable=(('U', NODAL, ((
    COMPONENT, 'U1'), )), ))
