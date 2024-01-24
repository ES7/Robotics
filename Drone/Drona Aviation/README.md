# Pluto Drone Swarm Challenge
Drona Aviation High Prep problem statement of InterIIT TechMeet 11.0 held at IIT Kanpur. This repository contains our attempted solutions and code for
all the 3 tasks of the problem statement. The first task was to make the pytohn wrapper for easy control of the drone during flying compared to earlier solutions of using
ROS or Pluto Drone App. Second task was to allow for setpoint navigation which can be hardcoded in the program initially, the drone is viewed by a camera on the s the Aruco Marker on top of the drone. Third task was to simultaneously control two drones which would make a rectangle in sync.
<br><br>
For more details go through the problem statement `DronaAviationPS.pdf`
<br><br>
## Task 1
This wrapper implements a communication pipeline between a laptop and Pluto drone using the **Telnet protocol**. The pipeline starts with a connection to the Pluto drone with a specified **host** and **port** through the **connect function**, which opens a Telnet connection and starts a new thread **monitorThread** to listen to incoming data from the drone. The data is received by the **monitorSerialPort** function and parsed into individual messages consisting of a header, message size, command, data payload, and checksum. The parsed messages are stored in the responses dictionary. The pipeline can be terminated by calling the **disconnect function**, which stops the monitorThread and closes the Telnet connection.
<br>
* **sendData :** sends a packet of data over Telnet
* **waitForResponse :** waits until the requested data is received and then returns the data
* **encodePacket :** creates an MSP packet and sends it over the Telnet connection
* **getData :** encapsulates the process of sending a command to get data and returning the data when it is received
* **setRC :** sends RC values to the drone to control its flight
* **setCommand :** sends different commands to the drone to perform specific actions such as takeoff, landing, or flipping
* **setThrottle(value) :** Sets the throttle value of the quadcopter in PWM units with a range of 900 to 2100.
* **setPitch(value) :** Sets the pitch value of the quadcopter in PWM units with a range of 900 to 2100.
* **setRoll(value) :** Sets the roll value of the quadcopter in PWM units with a range of 900 to 2100.
* **setYaw(value) :** Sets the yaw value of the quadcopter in PWM units with a range of 900 to 2100.
* **ARM() :** Arms the quadcopter by setting a value of 1500 to the "aux4" channel.
* **DISARM() :** Disarms the quadcopter by setting a value of 1000 to the "aux4" channel.
* **AltitudeHold_ON() :** Turns on the altitude hold mode by setting a value of 1500 to the "aux3" channel.
* **AltitudeHold_OFF() :** Turns off the altitude hold mode by setting a value of 1000 to the "aux3" channel.
* **DevMode_ON() :** Turns on the developer mode by setting a value of 1500 to the "aux2" channel.
* **DevMode_OFF() :** Turns off the developer mode by setting a value of 1000 to the "aux2" channel.
* **HeadFree_ON() :** Turns on the head-free mode by setting a value of 1500 to the "aux1" channel.
* **HeadFree_OFF() :** Turns off the head-free mode by setting a value of 1000 to the "aux1" channel.
* **TakeOff() :** Commands the quadcopter to take off by calling the setCommand(1) method.
* **Land() :** Commands the quadcopter to land by calling the setCommand(2) method.
* **BackFlip() :** Commands the quadcopter to perform a backflip by calling the setCommand(3) method.
* **FrontFlip() :** Commands the quadcopter to perform a frontflip by calling the setCommand(4) method.
* **RightFlip() :** Commands the quadcopter to perform a rightflip by calling the setCommand(5) method.
* **LeftFlip() :** Commands the quadcopter to perform a leftflip by calling the setCommand(6) method.
* **getAltitude() :** Returns the estimated altitude of the quadcopter in centimeters.
* **getVariometer() :** Returns the estimated vertical velocity of the quadcopter in cm/s.
* **getAcc() :** Returns the raw data from the accelerometer of the quadcopter in the format [X-axis, Y-axis, Z-axis].
* **getGyro() :** Returns the raw data from the gyroscope of the quadcopter in the format [X-axis, Y-axis, Z-axis].
* **getMag() :** Returns the raw data from the magnetometer of the quadcopter in the format [X-axis, Y-axis, Z-axis].
* **getRoll() :** Returns the roll of the quadcopter in degrees.
* **getPitch() :** Returns the pitch of the quadcopter in degrees.
* **getYaw() :** Returns the yaw of the quadcopter in degrees.
