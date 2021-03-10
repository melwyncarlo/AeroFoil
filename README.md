# ![AeroFoil Logo](https://raw.githubusercontent.com/melwyncarlo/AeroFoil/main/AeroFoil_UI_Files/AeroFoil.svg)<br>AeroFoil - a FreeCAD Macro

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: AGPL v3](https://img.shields.io/github/license/melwyncarlo/AeroFoil)](https://github.com/melwyncarlo/AeroFoil/blob/main/LICENSE)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/melwyncarlo/AeroFoil)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 
<br> ![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/melwyncarlo/AeroFoil) 
[![Build Status](https://travis-ci.com/melwyncarlo/AeroFoil.svg?branch=main)](https://travis-ci.com/melwyncarlo/AeroFoil) 
![Codecov](https://img.shields.io/codecov/c/github/melwyncarlo/AeroFoil) 
<br> [![Total alerts](https://img.shields.io/lgtm/alerts/g/melwyncarlo/AeroFoil.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/melwyncarlo/AeroFoil/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/melwyncarlo/AeroFoil.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/melwyncarlo/AeroFoil/context:python)

----

**'AeroFoil'** is a user-created macro to be used within the [FreeCAD](https://www.freecadweb.org/) application.
AeroFoil creates airfoil curves and faces using pre-defined models, algebraic functions, 
as well as imported DAT or CSV files.

----


### <br>Key Features
* Airfoil points refinement
* Multiple airfoil copy generation
* 2D curves and planar face output
* DWire/PolyLine and BSpline output
* Sketcher workbench and Draft workbench output
* Fully constrained sketches in Sketcher workbench
* Split (upper and lower) airfoil curves generation
* Ready-made NACA 4-digit and 5-digit solvers
* Symmetric and asymmetric curve functions parser
* DAT text file and CSV spreadsheet data parser
* Chord length input in mm, cm, m, in., ft, and yards

### <br>Installation
In the [FreeCAD](https://www.freecadweb.org/) software, AeroFoil can be downloaded directly using the in-built [Addon Manager](https://wiki.freecadweb.org/Std_AddonMgr).
<br>AeroFoil can also be obtained from the [FreeCAD Macros Github Repository].

In Linux, AeroFoil can be installed manually, similar to Windows installation, or by using the command terminal and its relevant commands as mentioned in the [INSTALL](https://github.com/melwyncarlo/AeroFoil/blob/main/INSTALL.sh) file.

By default, the Linux command terminal can be launched by pressing the following keyboard keys simultaneously :
```
Control + Alt + T
```

In Windows, AeroFoil can be installed with the help of the following two steps :-
1. Download the [AeroFoil.zip](https://github.com/melwyncarlo/AeroFoil/blob/main/AeroFoil.zip) file.
2. Extract the ZIP file's contents into the FreeCAD User Macro directory location.

By default, the FreeCAD User Macro directory should be located at :
```
~/.FreeCAD/Macro
```

### <br>Usage
AeroFoil can be loaded by performing the following steps :-
1. Launch the `FreeCAD` application.
2. Click on the `Macro` menu from the Menu Bar.
3. Click on `Macros ...` from the Macro sub-menus.
4. Click on the `User macros` tab in the pop-up dialog box.
5. Select `AeroFoil.FCMacro`.
6. Click on the `Execute` button.

Once, the AeroFoil macro has been loaded, follow the instructions in the respective dialog boxes, fill in the relevant inputs, and navigate accordingly. In case of *error* or *warning*, you will automatically be notified of the same. In case you are notified to report an *unexpected error*, communicate the error by mentioning the FreeCAD version, tracing the steps taken, and mentioning whether (and how much) or not any ouput was generated.


|   | **Notes** |
| ------------- | ------------- |
| **(1)**  | Performing the macro operation with custom points and refinement produces no visible changes.  |
| **(2)**  | The AeroFoil object properties are only visible on the FreeCAD software version 0.19. On older versions, you will be shown a warning on the console. This warning will not affect the output.  |

For more information on the AeroFoil macro, refer to its [FreeCAD Macro Wiki Page](http://www.freecadweb.org/wiki/index.php?title=Macro_AeroFoil) or its discussion page on the [FreeCAD Forum](https://forum.freecadweb.org/viewtopic.php?f=22&t=56162).

### <br>Future works
- [X] Fix Bugs (for FreeCAD v0.18 and v0.19)
- [X] Get the LGTM Alerts to 0, and Code Quality to A
- [ ] Add Leading Edge Refinement (0c to 0.25c)
- [X] Add the AeroFoil icon to the dialog boxes
- [ ] Add the AeroFoil icon to objects in Tree View
- [ ] Convert from Part :: Feature object to App :: FeaturePython object
- [ ] Attempt, if possible, a complete CodeCov Coverage
- [ ] Separate the 'AeroFoil' and 'AeroFoilDialog' classes into two files
- [ ] Create a Python Console Run Command

### <br>License
AeroFoil is made available under the [GNU Lesser General Public License Version 2.1](https://github.com/melwyncarlo/AeroFoil/blob/main/LICENSE).
