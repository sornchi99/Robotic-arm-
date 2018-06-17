#!/usr/bin/env python
from nanpy import(ArduinoApi,SerialManager) # Hardware serial control  
from nanpy import Servo   # Servo controller 
import Tkinter
import math 
from Tkinter import* # Import GUI function for error port alert 
connection = SerialManager('/dev/ttyACM0',115200) # Serial connection 
a = ArduinoApi(connection=connection)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
def RunServo(event): 
     Bases.write(Base.get())
     print(Base.get())
def RunServo1(event): 
     Shoulders.write(Shoulder.get())
     print(Shoulder.get())
def RunServo2(event):
     Elbows.write(Elbow.get())
     print(Elbow.get())
def RunServo3(event):
     WristRots.write(WristRot.get())
     print(WristRot.get())
def RunServo4(event):
     Wrists.write(Wrist.get())
     print(Wrist.get())
def RunServo5(event):
     Grippers.write(Gripper.get())
     print(Gripper.get())        
def kinematicbase(event):  # get the base angle to control kinematic function
     AngleBaseoutput = math.degrees(math.atan(y.get()/x.get())) #base
     Base.write(AngleBaseoutput)
def Shoulder(event):   # manipulator control function of Shouldr 
     AngleShoulderoutput = math.degrees(math.asin((z.get()+100)/120)) #Shoulder
     Shoulder.write(AngleShoulderoutput)
def Elbow(event):     
     AngleElbowoutput = math.degrees(math.acos(((math.pow(120,2)+math.pow(120,2))-(math.pow(x.get(),2)+math.pow(y.get(),2)))/(2*120*120))) #Elbow
     Elbow.write(AngleElbowoutput) 
def Wrist(event):
     AngleWristoutput = (180-(math.degrees(math.asin((z.get()+100)/120)))-(math.degrees(math.acos(((math.pow(120,2)+math.pow(120,2))-(math.pow(x.get(),2)+math.pow(y.get(),2)))/(2*120*120)))))
     Wrist.write(AngleWristoutput)
def WristRot(event):
     AngleWristRotoutput = WristsRots.write(WristRot.get())
     WristRot.write(AngleWristRotoutput)
def Gripper(event):
     AngleGripperoutput = Grippers.write(Gripper.get())
     Gripper.write(AngleGripperoutput)                    

       # Servo controller pin 
Bases = Servo(2) 
Shoulders = Servo(3)
Elbows = Servo(4)
WristRots = Servo(5)
Wrists = Servo(8)
Grippers = Servo(9)
Master = Tk()
# Base set scale
Base = Scale(Master,from_=0,to=180, orient=HORIZONTAL,command=RunServo)
Base.set(0)
Base.pack()
Shoulder = Scale(Master,from_=0,to=180, orient=HORIZONTAL,command=RunServo1)
Shoulder.set(0)
Shoulder.pack()
Elbow = Scale(Master,from_=0,to=180, orient=HORIZONTAL,command=RunServo2)
Elbow.set(0)
Elbow.pack()
WristRot = Scale(Master,from_=0,to=180, orient=HORIZONTAL,command=RunServo3)
WristRot.set(0)
WristRot.pack()
Wrist = Scale(Master,from_=0,to=180, orient=HORIZONTAL,command=RunServo4)
Wrist.set(0)
Wrist.pack()
Gripper = Scale(Master,from_=0,to=180, orient=HORIZONTAL,command=RunServo5)
Gripper.set(0)
Gripper.pack()
X = Scale(Master,from_=0,to=500, orient=HORIZONTAL,command=kinematicbase)
X.set(0)
X.pack()
Y = Scale(Master,from_=0,to=500, orient=HORIZONTAL,command=Kinematicbase)
Y.set(0)
Y.pack()
Z = Scale(Master,from_=0,to=500, orient=HORIZONTAL,command=)
Z.set(0)
Z.pack()

button1 = Button(Master,text = "Control1",fg = 'blue',command=RunServo,activebackground = 'red')
button1.pack()
button2 = Button(Master,text = "Control2",fg = 'blue',command=RunServo1,activebackground = 'green')
button2.pack()
button3 = Button(Master,text = "Control3",fg = 'blue',command=RunServo2,activebackground = 'pink')
button3.pack()
button4 = Button(Master,text = "Control4",fg = 'blue',command=RunServo3,activebackground = 'blue')
button4.pack()
button5 = Button(Master,text = "Control5",fg = 'blue',command=RunServo4,activebackground = 'brown')
button5.pack()
button6 = Button(Master,text = "Control6",fg = 'blue',command=RunServo5,activebackground = 'black')
button6.pack()
mainloop()

while(True): 
      # Angle Analoginput and show the value of the angle 
     AngleBase  = (a.analogRead(0))*0.175953079 # Angle transformation conversion 
     AngleShoulder = (a.analogRead(1))*0.175953079
     AngleElbow = (a.analogRead(2))*0.175953079
     AngleWristRot = (a.analogRead(3))*0.175953079
     AngleWrist  = (a.analogRead(4))*0.175953079
     AngleGripper = (a.analogRead(5))*0.175953079
     print(AngleBase,AngleShoulder,AngleElbow,AngleWristRot,AngleWrist,AngleGripper)
