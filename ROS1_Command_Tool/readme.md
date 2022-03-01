# Note of ROS1

ROS System: Kinetic
Python Version: Python 3.5
Ubuntu Version: 

## 1. Catkin_make
### 'catkin_make -DPYTHON_EXECUTABLE:FILEPATH= xxx/xxx'

```catkin_make -DPYTHON_EXECUTABLE:FILEPATH=/home/user/.py3venv/bin/python```

This command is to indicator which python interpreter we are going to use to build the ROS package.

## 2. Command Tools

### `rospack profile`

The main function of rospack is to crawl through the packages in ROS_ROOT and ROS_PACKAGE_PATH, read and parse the 
manifest.xml for each package, and assemble a complete dependency tree for all packages.

rospack’s performance can be adversely affected by the presence of very broad and/or deep directory structures that
don’t contain manifest files. If such directories are in rospack’s search path, it can spend a lot of time crawling 
them only to discover that there are no packages to be found. You can prevent this latency by creating a 
rospack_nosubdirs file in such directories. If rospack seems to be running annoyingly slowly, you can use the profile 
command, which will print out the 20 slowest trees to crawl (or use profile --length=N to print the slowest N trees).