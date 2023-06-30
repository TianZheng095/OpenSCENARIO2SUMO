# OpenSCENARIO2SUMO
Automatic traffic scenario conversion interface between OpenSCENARIO and the traffic simulator SUMO. Currently, only the conversion from **O**pen**SC**ENARIO to **C**ommon**R**OAD (osc2cr) is developed.<br>

### Code Reference
This repo refers to 
1. [Commonroad Scenario Designer](https://gitlab.lrz.de/tum-cps/commonroad-scenario-designer.git)
2. [CommonROAD-OpenSCENARIO Converter](https://gitlab.lrz.de/tum-cps/commonroad-openscenario-converter.git)

### Requirements
The code is written in Python 3.10 and has been tested on Ubuntu 22.04. 

If you want to use the SUMO conversion or to generate traffic using SUMO, please install 
[SUMO](https://sumo.dlr.de/docs/index.html):
```bash
sudo apt-get update
sudo apt-get install sumo sumo-tools sumo-doc
echo "export SUMO_HOME=/usr/share/sumo" >> ~/.bashrc
echo 'export PYTHONPATH="$SUMO_HOME/tools:$PYTHONPATH"' >> ~/.bashrc
```
If you use zsh, replace `.bashrc` with `.zshrc`.


### Using the CommonRoad Scenario Designer
The recommended way of installation if you only want to use the scenario designer (i.e., you do not want to work with the code directly) is to use the PyPI package:
```bash
pip install commonroad-scenario-designer
```


### Common Errors during installation

- **Could not load the Qt platform plugin “xcb” in “” even though it was found:** Error seems to be a missing package - either libxkbcommon-x11 or libxcb-xinerama0 (both can be installed by ```sudo apt install [package_name]```). See for reference [here](https://discuss.pixls.us/t/solved-could-not-load-the-qt-platform-plugin-xcb-in-even-though-it-was-found/17677/9)




### GUI Usage

The GUI can either be activated via the command line via the following two options:

```bash
$ crdesigner
$ crdesigner gui
```
Note that you have to activate first the Python environment in which the CommonRoad Scenario Designer is installed.





### Openscenario to Commonroad Converter
We recommend using [Anaconda](https://www.anaconda.com/) to manage your environment so that
even if you mess something up, you can always have a safe and clean restart. 
A guide for managing Python environments with Anaconda can be found [here](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

- First, clone the repository. 
- After installing Anaconda, create a new environment with (>=3.9) and enter it:
``` bash
$ conda create -n commonroad-py39 python=3.9 -y
$ conda activate commonroad-py39
```
- Then, install the dependencies with:

```bash
$ pip install commonroad-openscenario-converter
```

- Test case:
```bash
$ cd test
$ python OSC_Convert2_CR.py
```
The generated simple curve scenario "OpenSCENRAIO2SUMO/output/SimpleCurve/OSC_SimpleCurve_1_T-1.xml" could be opened via the CommonRoad Scenario Designer.

### Open Commonroad file with crdesigner GUI 
Open the generated .xml file using the crdesigner GUI

![pics/openfileGUI.png](https://github.com/TianZheng095/OpenSCENARIO2SUMO/blob/main/pics/openfileGUI)

There are some redundant roads generated from Openscenario to Commonroad. They are able to be removed in this GUI to achieve a better and more reasonable conversion to SUMO later.
![pics/originalCircle.png](https://github.com/TianZheng095/OpenSCENARIO2SUMO/blob/main/pics/originalCircle.png)
![pics/modifiedCircle.png](https://github.com/TianZheng095/OpenSCENARIO2SUMO/blob/main/pics/modifiedCircle.png)




### Paper Reference
1. [CommonRoad Scenario Designer: An Open-Source Toolbox for Map Conversion and Scenario Creation for Autonomous Vehicles](https://arxiv.org/pdf/2305.10080.pdf)
2. [Automatic Traffic Scenario Conversion from OpenSCENARIO to CommonRoad](https://arxiv.org/pdf/2305.10080.pdf)
