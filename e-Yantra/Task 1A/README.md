# Stablising the Swift Drone
**Aim :-** The aim of this task is to build a PID control system to stabilise the Swift Drone at any given position in a simulation environment in Gazebo.  <br>

**Prerequisites :-** It is presumed that you have successfully completed Task 0 and completed the codechef challenge. Also this task involves writing programs in Python programming language, so get acquainted with the basics of Python and ROS libraries for Pyhton. Follow the given resources to get started with the topics and do not limit yourself with the resources listed, internet is a vast ocean of knowledge, make use of it ! <br>

**Installations :-** Before proceeding further, you need to install the some softwares and packages. To do that, follow these commands: <br>
1. Create a catkin workspace <br>
_`cd` <br>
`mkdir catkin_ws/src -p` <br>
`cd catkin_ws` <br>
`catkin init`_ <br>

2. Build your workspace <br>
_`cd ~/catkin_ws` <br>
`catkin build`_ <br>

3. Each time you build your workspace, you need to source `setup.bash` file from the `catkin_ws/devel` folder. Instead of doing this manually, let us add a line in `.bashrc`. <br>
_`echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc`_ <br>

4. Now clone the luminosity_drone and other ros packages form GitHub <br>
_`cd ~/catkin_ws/src` <br>
`git clone https://github.com/eYantra-Robotics-Competition/luminosity_drone --recursive` <br>
`git clone https://github.com/simmubhangu/pid_tune`_ <br>

5. Install dependencies <br>
_`sudo apt install python-tk ros-noetic-octomap-msgs ros-noetic-octomap-ros ros-noetic-mavlink libgoogle-glog-dev ros-noetic-plotjuggler-ros`_ <br>

6. Now build your workspace <br>
_`cd ~/catkin_ws` <br>
`catkin build` <br>
`source ~/.bashrc`_ <br>

**Problem Statement** <br>
* The task is to build a PID controller for controlling position (x,y,z) of the swift drone in Gazebo world.
* The output of the controller will be commands to the swift drone as angle-setpoints which the swift drone is supposed to tilt at.
* The PID controller will be written as a rosnode written in python programming language.
* After the PID controller is build and tuned successfully, the swift drone should be able to move and stabilise at the given setpoint [2,2,20] in the gazebo environment and stay within the error range of ±0.2m in all the coordinates.

**Procedure** <br>
* Launch the Gazebo world containing the swift drone and the overhead camera by typing the following command:
_`roslaunch luminosity_drone task_1.launch`_ <br>
