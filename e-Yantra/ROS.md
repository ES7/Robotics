## I have learned ROS to complete the tasks for Eyantra (Luminosity Drone)
**Theme :-** Luminosity Drone (LD)<br>
**Technology Stacks :** Drone Building, Control Systems, Position control & Waypoint navigation, Image processing.<br>
**Tools and Technologies :** Robot Operating System (ROS), Gazebo simulation, Python programming, OpenCV<br>

**System Requirements :**
**Operating System :** Ubuntu 22.04 LTS<br>
**Processor :** i5 8th gen or above / equivalent<br>
**HDD or SSD Storage space :** 50GB or more<br>
**RAM :** 8GB or more<br>

## Linux
- Linux is a family of open source and community-developed operating systems which is widely used in computers, servers, mainframes, mobile devices and embedded devices.
- Linux is a UNIX-style operating system written in C and Assembly by Linus Trovalds and Linux Community.
- There are many flavors of Linux OS like, Debian, Ubuntu, Arch, Kali, Linux Mint.
- Both Linux and macOS are UNIX based OS whereas modern Windows OSes are NT based.
- In this eYRC Theme we are going to use Ubuntu 20.04.

### Linux File System Directories
- **`root`** is the beginning or the top point of the Unix File System under which directories important to a Unix OS resides. It is different from a root user of the system.
- Each directory contains a set of files and programs which are required for the proper functioning of the OS.
- Out of all the directories, **`/home/`** and **`/opt/`** are two important directories for this eYRC Theme.
- **`/opt/`** is the directory or folder where the packages or software which you are going to install using package manager (apt-get in Ubuntu) is going to reside.
- **`/home/`** is the folder where all your personal files including project files are going to reside.
- **`/bin/`** is the folder where most common Linux commands reside. Commands like ls, chmodetc.

### Linux File System Types :- ext, ext2, ext3, JFS, XFSbtrfs, swap.
- **Ext :-** "extended file system" was the very 1st file system designed for Linux. To overcome the limitations of the MINIX file system.
- **Ext2 :-** "2d extended system" innovated in areas such as storage capacity, general performance. Allows upto 2 TB of data.
- **Ext3 :-** "3rd extended system" is a journaling file system, which records in a separate log changes and updates to files and data before such actions have been completed. Means if the computer crashes then this separate log containing the changes made before crash can be used to access the stored data, thus repairing and restoring the files upon reboot.
- **Ext4 :-** "4th extended system" this system overcomes numerous limitations.
- **JFS :-** "Journaling File System" easy to recover data after crash. Uses less CPU power than the other file systems.
- **XFS :-** 64-bit high performance journaling file system. It’s particularly noteworthy for how incredibly well it works with very large files. Though contrarily, not especially the best with smaller files.
- **Btrfs :-** "B Tree File System" it is a rival file system to ext4, transfers data faster and offers more stability. 
To check the file type go to the terminal and type :- **`$ df -T`**.

**`/`** is the top level directory of a Linux system. The name "top level" means the **"root"**, thus it is the root directory of the system. Though it is separate from **"/root directory"**, so we shouldn't confuse the two.
All other directories stem from this top level directory like a pyramid. This concept is not unique to Linux, as the same thing can be observed in other Operating Systems. Windows has partitions such as C: and D:.
In Linux, these directories in the so-called "pyramid" exist in a hierarchy with a specific structure. This can be observed in your terminal by using the command : **`$ cd /`**.
This command displays the directories and files while in the top level directory.

/bin – essential utilities :- The directory contains the core system programs and important utilities. For example, commonly used and well known commands such as “cat” are located in “/bin”. The reason for this is that if these utilities are not stored in this directory, there is no certainty that the system will have access to them if there isn’t a file system mounted. There is the directory /sbin that is very similar to /bin, as it contains core system administration binaries (programs).


**`/boot` – Boot for a Boot :-** Contains files that are required in order for the system to be booted. For example, BIOS, which stands for Basic Input/Output System. The BIOS is responsible for executing the Master Boot Record (MBR) boot loader. It checks the integrity of the hard disk(s) of the system before launching the MBR. /boot also contains Linux kernels and many other files in addition to BIOS. Though, these file’s configuration files are not stored in /boot, rather they are stored in /etc, along with the many other various config files.

**`/dev` – Devices or Files :-** Linux displays connected devices as files and the /dev directory contains these files. Though, the thing is, as we can see by the title, these are not “actual” files, they just appear as files. /dev is also where physical drives can be mounted.

**`/etc` – Configuration files :-** The configuration files of BIOS and other similar files can be found in /etc. We can edit these configuration files in a text editor. Basically, every single kind of configuration file is located in /etc, including but not limited to system configuration files.

**`/home` – Home Folder Containment :-** There’s a home folder for every user on the system and each one is contained together in the /home directory. These folders are created using the name of the user name. Home folder → /home/name.
These home folders contain your user data files and configuration files that are specific to the user, which is also the one of the only types of configuration files that are stored elsewhere besides /etc.<br>
**NOTE :-** If one wants to modify other files on a system, they must become the root user, as each user only has write permissions for their own home folder (/home/name).

**`/lib` – Libraries for Programs :-** Each program or binary uses specific libraries to function and the /lib directory is where these libraries can be located.

**`/media` – Mounted Media :-** Contains subdirectories where your physical media devices are mounted. For example, a CD, if inserted into our system, we can access its contents through its directory that is created in the /media directory upon insertion.

**`/mnt` – Temporary Mounts :-** This directory is used for mounting temporary file systems. If we are using a file system for a very specific purpose and for a relatively brief period of time, we would probably mount it in /mnt. Though we can mount it anywhere on the system if we so chose.

**`/opt` – Optional Packages :-** The /opt directory contains a set of subdirectories where optional software packages are located and managed by the package manager.

**`/proc` – Kernel and Process Pseudo Files :-** The /proc directory is another interesting case of a directory that contains these “fake” files, very similarly to the /dev directory. These files are special files that are actually, and interestingly, system and process information.

**`/root` – Root User Directory :-** Every user has his own home directory. This is the home directory of the root user. The root user’s home directory is located at /root. Which is noteworthy because it is, unlike the rest of the user’s home directories, not located in /home. /root is different from the root directory “/”, and this fact should be committed to memory if possible.

**`/sbin` – System Administration Programs :-** The /sbin directory is similar to the /bin directory in that it contains essential programs. But it differs with the addition that it is intended to be used by the root user.

**`/tmp` – Temporary Files :-** The /tmp directory is used to store temporary files that are deleted when the system is restarted. Utilities such as tmpwatch can be used to delete these temporary files in the /tmp directory.

**`/usr` – User Shared Read-Only Data :-** The /usr directory is used to contain applications and files that are used and shared by and between users.

**`/var` – Variable Data :-** The /var directory is used like the /usr directory, only instead of being read-only, it is writable. This directory contains system logs and other various variable data.

### Linux File Permissions
Like most of the modern operating systems, Linux is a multi-user OS hence an extra layer of security is added to prevent users from accessing each other's confidential files. 

Linux divides authorization into two levels :- **Ownership; Permission**.
Each file and directory has three user based permission groups :- **owner, group, all**
Each file or directory has three basic permission types :- **read, write, execute**

Linux File Permissions is a vast topic but we need not have to master it to succeed in this eYRC Theme. The only thing we need to keep in mind is that unlike Windows where programs with **.exe** extension can be executed, in **UNIX/Linux**, files with execute permission can only be executed/run by the user.

To make a file executable in Linux following command can be used,
**`sudo chmod +x <file_name>`**

### Linux Commands
**The Linux Terminal :-** In UNIX, a terminal is a text interface to interact with the OS. There is a list of commands which users can use to interact with the OS. Terminal is also called a **shell** or **console**.<br>
**Command Prompt** and **Powershell** are two such interfaces provided by Windows OS.<br>
In **Ubuntu** and most of the UNIX based OS a particular type of shell called **Bash** which is one kind of UNIX shell, is launched when you open any Terminal program. **Zsh** is another such popular shell for UNIX.<br>
These UNIX shells like Bash and Zsh are command processors which take commands from the user, interpret them and execute the commands with the help of the underlying OS.
UNIX shells can also read commands from a file. Such files are called Shell Scripts. In the next section we will explore this.<br>
One such shell script is **`.bashrc`** which resides in **`/home/directory`**. This shell script runs every time you open an instance of Bash shell.<br>
In Ubuntu you can press **`Ctrl+Alt+T`** to open up an instance of the terminal.

### Common Linux Commands
**sudo**<br>
In UNIX a superuser or root is a user which has unrestricted access to all the commands, files, folders and resources of the system. If we want to run any command as a superuser we need to prefix that command with **sudo**.<br>
Eg : **`sudo chmod +x hello.sh`**.
- **`ls` :-** List the files and folders in the current directory.
**`ls -l` :- -l flag** is used with ls to list files and folders in the current directory with their permissions.<br>
**`ls -la` :- -la flag** is used to list all the files and folders including hidden ones with their permissions.<br>
- **`mkdir folder1 folder2` :-** this command will create 2 folders, folder1 & folder2 in the current directory.
• **`cd ~` :-** this will take to /home/directory. In UNIX, tilde ~ is used to represent home directory.<br>
**`cd ~/catkin_ws` :-** this will take us inside a folder named catkin_ws in the home directory. 
- **`echo "hello"` :-** this will print the string hello in the terminal.<br>
**`echo “hello” >> file.txt` :-** this will append the string hello at the end of file.txt. This won’t overwrite anything.<br>
**`echo “hello” > file.txt` :-** this will append the string hello at the beginning of the file.txt. This will overwrite.
- **`find . -type d -name "dir_name_start*"` :-** list the files and folders in the current directory starting with "dir_nam_start".<br>
**`find . -type f -name "file_name.*"` :-** search for files starting with "file_name" with unknown extension.
- **`grep -rnw "text"` :-** search for “text” string inside any type of file.
**`catkin build | grep "pkg_my_ros"` :-** highlight and show only the pre-defined text in the output of a command. 
- **`which python` :-** this command is used to find the location of an executable available to shell.
- **`pwd` :-** this will print the path of the current directory we are in.
- **`cat -n file.txt` :-** this will print the content of file.txt with line numbers, in the terminal.
- **`man` :-** use full command in UNIX, if we are not sure how to use any command then just call this like :  man which.

### ROS (Robot Operating System)
ROS is an open-source framework and middleware specifically designed to develop and control robots. Despite its name, ROS is not a traditional operating system like Windows or Linux. Instead, it provides a set of tools, libraries, and conventions for building and managing complex robot applications.<br> 
ROS offers a modular and distributed architecture that facilitates communication between different components of a robot system. This includes sensors, actuators, control algorithms, planning algorithms, visualization tools, and more.

**ROS Tutorials :-** http://wiki.ros.org/ROS/Tutorials
**ROS Installation :-** http://wiki.ros.org/ROS/Installation

**Managing Environvment**
During the installation of ROS, we will see that we are prompted to source one of several setup.*sh files, or even add this 'sourcing' to our shell startup script. This is required because ROS relies on the notion of combining spaces using the shell environment. This makes developing against different versions of ROS or against different sets of packages easier.<br>
If we are ever having problems finding or using our ROS packages make sure that we have our environment properly set up. A good way to check is to ensure that environment variables like ROS_ROOT and ROS_PACKAGE_PATH are set : **`$ printenv | grep ROS`**<br>
If they are not then we might need to **'source'** some **`setup.*sh`** files.
Environment setup files are generated for us, but can come from different places :<br>
- ROS packages installed with package managers provide setup.*sh files.
- rosbuild workspaces provide setup.*sh files using tools like rosws.
- Setup.*sh files are created as a by-product of building or installing catkin packages.
If we just installed ROS from apt on Ubuntu then we will have setup.*sh files in **'`/opt/ros/<distro>/`'**, and we could source them like so : **`$ source /opt/ros/<distro>/setup.bash`**<br>
Using the short name of our ROS distribution instead of <distro>. If we have installed ROS Kinetic, that would be : **`$ source /opt/ros/kinetic/setup.bash`**<br>
We will need to run this command on every new shell we open to have access to the ROS commands, unless we add this line to our **.bashrc**. This process allows us to install serval ROS distributions (eg. indigo and kinetic) on the same computer and switch between them. On other platforms we will find these setup.*sh files wherever we have installed ROS.
