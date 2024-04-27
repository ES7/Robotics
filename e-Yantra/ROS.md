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
- **Ext :-** “extended file system” was the very 1st file system designed for Linux. To overcome the limitations of the MINIX file system.
- **Ext2 :-** “2d extended system” innovated in areas such as storage capacity, general performance. Allows upto 2 TB of data.
- **Ext3 :-** “3rd extended system” is a journaling file system, which records in a separate log changes and updates to files and data before such actions have been completed. Means if the computer crashes then this separate log containing the changes made before crash can be used to access the stored data, thus repairing and restoring the files upon reboot.
- **Ext4 :-** “4th extended system” this system overcomes numerous limitations.
- **JFS :-** “Journaling File System” easy to recover data after crash. Uses less CPU power than the other file systems.
- **XFS :-** 64-bit high performance journaling file system. It’s particularly noteworthy for how incredibly well it works with very large files. Though contrarily, not especially the best with smaller files.
- **Btrfs :-** “B Tree File System” it is a rival file system to ext4, transfers data faster and offers more stability. 
- To check the file type go to the terminal and type :- **`$ df -T`**.
