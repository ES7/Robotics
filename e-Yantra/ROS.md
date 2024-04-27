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
These home folders contain your user data files and configuration files that are specific to the user, which is also the one of the only types of configuration files that are stored elsewhere besides /etc.
**NOTE :-** If one wants to modify other files on a system, they must become the root user, as each user only has write permissions for their own home folder.

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
