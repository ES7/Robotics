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
<br><br>
## Task 2
For the identification and tracking of drones in mid-air, a single monocular camera from the top-view has been used. Specs of the camera used by us are as follows :<br>
**Fps : 60** <br>
It is responsible for tracking the position of the drone. The position of the drone is estimated by the aruco marker that is stuck on the top of the drone.  We have used a 4X4 Aruco Marker for this task. The camera is calibrated to estimate the x,y and depth values of the aruco marker. <br>
Detection of the aruco is done using the OpenCV library. The coordinates of the aruco marker obtained by the camera is then transformed to the coordinates with respect to the drone as to command the drone, it needs the points in its frame. <br>
The values of the **roll, pitch, yaw** and **throttle** of the drone is calculated using a PID controller. The **PID algorithm** is applied to the drone which involves calculating the error values, derivatives in order to get the proportional, derivative and integral output. It was a tedious task as it took a long time for us to get the correct **PD values**. Finally we got the approx values to make our drone hover.<br>
Correct values of the roll, pitch, yaw and throttle determined were feeded to the drone using the previous task script(python wrapper) to communicate with the drone. Now, to move the drone in a **rectangular trajectory**, the edge points of the rectangular shape were given to the drone as the setpoints. As the drone reaches to one setpoint, the drone hovers over that point till some set limit and then the next point is feeded automatically. <br>
<br>
In the `Image Capturing.py` file we click the images of the 7X7 chessboard. Then checking if the “images” directory exists or not, if it does not exist then create it. Then creating a user defined function detect_checker_board() to detect the chessboard in an image.inside this function we use cv.findChessboardCorners() and pass a grayscale image of the chessboard and its dimension. If the board is detected in the image then we draw the corners of the chessboard using cv.drawChessboardCorners() and return this image. Each frames that we get from the camera is converted into grayscale images and we pass these images into the detect_checker_board() function, this function return the image with corners drawn on it so we additionally add a text to it using cv.putText() as “saved_img”. Images are saved by clicking the ‘s’ key of the keyboard.<br>
<br>
In the `Cam Calliberation.py` file we first define the chessboard dimension and square size in millimeters, then we check the path of the directory where the calibrated data will be saved, if the directory is not existing then we create one. Then we use the images that were saved from the Image Capturing.py script to again detect and draw the corners of the chessboard. Then we calibrate the camera using cv.caliberateCamera() function and pass the 3D object points, 2D object points and grayscale image. This function returns the camera matrix, distance coefficient, translation vector and rotation vector. And finally then we load all this data into the **calib_data.npz** file.
<br><br>
In the `Distance Measurment.py` file we use this calib_data.npz file, load its data, define the aruco marker size in centimeters, then we detected the marker from the frames that we are capturing from the camera, if the marker is detected then we estimate its position using cv.estimatePoseSingleMarkers() and pass marker corners, marker size, camera matrix and distance coefficient and then we draw the boundary of the marker and its axes using cv.polyLines() and cv.drawFrameAxes(). Then using the translation vector we get the distance that is the z coordinate of the marker from the plane of the camera and then we add text i.e., ID number and Distance to each frame.
<br><br>
## Task 3
**Communication with 2nd drone :** <br>
This code is an example of **ESP32 code written in C++ using the Arduino IDE**. It sets up a connection to a Wi-Fi network with the **SSID** and **password**. The code uses the built-in LED on the ESP32 board and blinks it until the device successfully connects to the Wi-Fi network. <br>
Once connected, the code sets up a **client connection** to a server located at **IP address 192.168.4.1** and **port 23**. The loop function reads incoming data from both the serial connection and the client connection, and writes the received data to the other connection. It flushes the client connection and stops it after the data has been sent.<br>
* First the camera object is initialized with the required parameters of detection and camera specification. Both drone objects with their respective communication protocol are defined along with the sampling time of their pid and their initial setpoint. Then a list of Rectangle corner coordinates is supplied to the first PlutoPluto drone.
* Then the camera object member function is run in a loop which takes camera feed, detects the provided aruco markers, estimates their position, showing camera image feed, and updates the detected aruco position as a dictionary with their corresponding aruco id as key. This function also returns a “success” dictionary which contains boolean values for the provided aruco ids as keys of whether they are detected in that frame or not.
* These values of aruco id position are then fed to their corresponding drone object controller function. this controller function will make the drone to reach the setpoint
* First, the first drone will take off and reach the lower right corner(depending on the order of the rectangle corner list provided to it) of the rectangle and stay there for some time. After that the follower drone will fly and will acquire the (0, 0) position of the rectangle.
* After the follower drone hold its position for sometime, the first drone will change its setpoint and goes to the lower left corner of the rectangle
* After the first drone holds its position for some time, the follower drone will now move to the previous setpoint of the first drone i.e. at the lower right corner of the rectangle.
* After the follower drone holds its position for some time, the first drone will change its setpoint to the upper left corner of the rectangle and move there.
* This alternate cycle will keep on going until the first drone reach its final setpoint(as provided list, in our case we set the last setpoint (0,0) of rectangle) and the follower drone move to the previous setpoint of the first drone(i.e. previous point of (0,0) of rectangle i.e. lower right corner of rectangle).
* After that both drones will finally land.
The main theme of this task is that, a set of points will be provided only to the first drone, and the follower drone will chase the previous setpoint of the current setpoint of the first drone. this movement will take alternatively.
<br><br>

## Final Result and Conclusion
**Task 1 :-** Our idea and application achieved drone take-off easily with the Python wrapper we created. Only common problems with implementation were faced which were cleared through some trial and error. By then, we successfully connected the drone with our wrapper and sent MSP packets. <br>
**Task 2 :-** With a lot of failed attempts we finally got the drone doing what it was meant to. Drone followed the coordinates which were feeded, smoothly while maintaining a fixed altitude. This was achieved by using a single camera. Position control was fine tuned with different PID gau  Now we could control Pluto’s height and position. <br>
**Task 3 :-** Second drone successfully communicated with the wrapper through an external WiFi device(ESP32 board with a ping of approx. 100ms) and was made to follow the first drone. But the drone provided to us was defective and was unable to properly takeoff above some altitude. This restricted us to proceed further and test our code. The hardware issue couldn’t be fixed in the limited time. Hence the script was tested even with the faulty drone provided by the company. The script was working nicely and should work with a functional drone. <br>
