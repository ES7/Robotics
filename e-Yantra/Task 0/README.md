# Software Installations

**1. Ubuntu 20.04 Installation** <br>
installation Link :- https://releases.ubuntu.com/focal/ <br>
We will use Ubuntu 20.04 operating system (do not use any kind of virtual machines or Windows Subsystem for Linux (WSL) as we do not recommend and we wont be providing support). You can follow any tutorial on internet or YouTube to dual boot your system and install Ubuntu 20.04 alongside your existing operating system.

**2. ROS Installation**<br>
First thing after installing a fresh Ubuntu os is upgrading your system to the latest one, to do that, open a terminal, to open one, press Ctrl+Alt+t on your keyboard and type these commands carefully and press enter to execute a command. <br>
`_sudo apt upgrade_` <br>

Setup your computer to accept software from packages.ros.org. <br>
_sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'_ <br>

**Set up your keys**<br>
_sudo apt install curl # if you haven't already installed curl <br>
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -_ <br>

**Installation** <br>
_sudo apt update_ <br>
_sudo apt install ros-noetic-desktop-full_ <br>

**Environment setup** <br>
You must source this script in every bash terminal you use ROS in<br>
_source /opt/ros/noetic/setup.bash_<br>

It can be convenient to automatically source this script every time a new shell is launched. These commands will do that for you <br>
_echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc <br>
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc_ <br>
_source ~/.bashrc_ <br>

**Dependencies for building packages**<br>
_sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential python3-catkin-tools_ <br>

**Initialize rosdep** <br>
_sudo apt install python3-rosdep_ <br>

With the following, you can initalize rosdep
_sudo roesdep init <br>
rosdep update_ <br>

After this you have successfully installed **Ubuntu 20.04 LTS** and **ROS1 Noetic**.<br>
