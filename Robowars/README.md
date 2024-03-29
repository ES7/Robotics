# Robowars Bot
Robowars event of Concetto 23 held at IIT ISM Dhanbad by RoboISM club.<br>

# Designing
![Screenshot 2024-01-25 164140](https://github.com/ES7/Robotics/assets/95970293/b2bee2c6-daf2-4843-a25f-94d153a2b1fc)
Initial design of the bot that we thought was very simple, 2 wheeled bot with a simple cutter on it. This design was cheap to build but it has many flaws like wheels are exposed, body made of wood, and the weapon is prone to break as it has no support. <br>
After this we came up with another design, and this time we tried to solve the problems that we faced in the last design. We designed the chassis in such a way so that the wheels are inside and on the back side of the chassis far from center of gravity, reducing their grip. A very large and thin double vertical spinner is prone to breaking at the narrow point on impact. The weapon is supported by 3 bearings (aluminum housing). These are also prone to breaking. The shaft is of SS but only 8mm in diameter which is also prone to breaking. There were still some issues with this design so we tried another design from scratch. <br>
This time we tried a symmetric design, so that even if it gets flipped upside down it will still work. But there are issues in this, there is not much interlocking between the metal and wood. The center of the bot has no metal parts, making it very weak. The wheels are exposed from behind. So then the final design was like a rectangular box with a wedged drum attached on the front part. This design features interlocking between wood and metal pieces. The weapon is supported sufficiently as the shaft passes through the two central mild steel plates. The plates are held together by interlocking but the major strength factor lies in the fact that m5 rods have been fed through all the 4 plates, with lock nuts on each side of every plate for all the threads, forming a metal skeleton. Truss type structures have been used in the two internal metal plates to ensure strength without much weight gain. Wheels are guarded, it is a symmetric design  so can work even flipped. Wood has been used only in those parts of the bot that are least likely to take an impact, thus maximum weight can be diverted into armor and weapon.<br> 
<br>
![Screenshot 2024-01-25 163845](https://github.com/ES7/Robotics/assets/95970293/077e1cee-1e5f-4c33-bbc8-641638d512b9)
![Screenshot 2024-01-25 163910](https://github.com/ES7/Robotics/assets/95970293/3fc06dbe-78a2-47d1-80fb-13d0316e45c1)
The weapon consists of multiple 5mm thick pieces of mild steel, each circular piece adopts a flywheel type design  (weight away from the axis to maximize inertia) This will allow the weapon to store more energy at maximum RPM, resulting in a more devastating hit!. Note that since the center of the shaft is prismatic, all the circular pieces act as a single piece.<br>
![Screenshot 2024-01-25 163814](https://github.com/ES7/Robotics/assets/95970293/502f8aa2-553b-4606-9bd5-8447811b0103)

# Manufacturing
For Wood : Diagrams were given to a carpenter. <br>
For Metal : Export as dxf file tool was used in fusion 360, for the side plates, mid plates, and circular discs of the weapon, these files were sent to Robu.in laser cutting service, and the parts were received 2 days later. <br>
For Shaft : a Lathe machine, and milling machine were used to create the shaft (finishing was required). All screws, bolts, bearings, belts,wheels etc were purchased online. The main structure was assembled in the Roboism club room. <br>

# Electronics
Motor drivers used are dual bts7960 H-bridge drivers (rated for 43A) for the wheels, for the weapon motor, a 5v relay was controlled by the arduino.(Also mosfets dont work...) A 2200mah li-Ion battery of 24V was used along with a BMS to power the bot. Using the NRF24 for RF communication can be a bit tricky, and there are videos online on how to use them properly. The NRF24 was used as it has a good data rate for the number of channels it supports, and it has a good range with the antenna. 
