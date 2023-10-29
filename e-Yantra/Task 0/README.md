# Software Installations

**1. Ubuntu 20.04 Installation** <br>
installation Link :- https://releases.ubuntu.com/focal/ <br>
We will use Ubuntu 20.04 operating system (do not use any kind of virtual machines or Windows Subsystem for Linux (WSL) as we do not recommend and we wont be providing support). You can follow any tutorial on internet or YouTube to dual boot your system and install Ubuntu 20.04 alongside your existing operating system.

**2. ROS Installation**<br>
First thing after installing a fresh Ubuntu os is upgrading your system to the latest one, to do that, open a terminal, to open one, press Ctrl+Alt+t on your keyboard and type these commands carefully and press enter to execute a command. <br>
_`sudo apt upgrade`_ <br>

Setup your computer to accept software from packages.ros.org. <br>
_`sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'`_ <br>

**Set up your keys**<br>
_`sudo apt install curl # if you haven't already installed curl <br>
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -`_ <br>

**Installation** <br>
_`sudo apt update`_ <br>
_`sudo apt install ros-noetic-desktop-full`_ <br>

**Environment setup** <br>
You must source this script in every bash terminal you use ROS in<br>
_`source /opt/ros/noetic/setup.bash`_<br>

It can be convenient to automatically source this script every time a new shell is launched. These commands will do that for you <br>
_`echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc <br>
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc`_ <br>
_`source ~/.bashrc`_ <br>

**Dependencies for building packages**<br>
_`sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential python3-catkin-tools`_ <br>

**Initialize rosdep** <br>
_`sudo apt install python3-rosdep`_ <br>

With the following, you can initalize rosdep <br>
_`sudo roesdep init <br>
rosdep update`_ <br>

After this you have successfully installed **Ubuntu 20.04 LTS** and **ROS1 Noetic**.<br>
