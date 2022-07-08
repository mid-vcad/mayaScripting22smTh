import maya.cmds as cmds
#Create a variable called "size" and set to 10
size = 10
#Create a polySphere, name it Sun, radius of "size" * 10.0
cmds.polySphere(n="Sun", r=size*10.0)
#Create a polySphere, name it Earth, radius of "size" * 1.0
cmds.polySphere(n="Earth", r=size*1.0)
#Create a polySphere, name it Moon, radius of "size" * 0.3
cmds.polySphere(n="Moon", r=size*0.3)
#Create a Circle, name it “Sun_Ctrl”, radius of "size" * 11.0, aim vector on Y
cmds.circle(n="Sun_Ctrl", nr=(0,1,0), r = size * 11.0)
#Create a Circle, name it “Earth_Ctrl”, radius of "size" * 1.1, aim vector on Y
cmds.circle(n="Earth_Ctrl", nr=(0,1,0), r = size * 1.1)
#Create a Circle, name it “Moon_Ctrl”, radius of "size" * 0.33, aim vector on Y
cmds.circle(n="Moon_Ctrl", nr=(0,1,0), r = size * 0.33)
#color “Sun_Ctrl” to yellow
cmds.color("Sun_Ctrl", rgb=(1,1,0))
#color “Earth_Ctrl” to blue (0, 0, 1)
#color “Moon_Ctrl” to grey (0.5, 0.5, 0.5)
#parent “Sun” under “Sun_Ctrl”
cmds.parent("Earth", "Earth_Ctrl")
#parent “Earth” under “Earth_Ctrl”
cmds.parent("Earth", "Earth_Ctrl")
#parent “Moon” under “Moon_Ctrl”
cmds.parent("Earth", "Earth_Ctrl")
#parent “Earth_Ctrl” under “Sun_Ctrl”
cmds.parent("Earth", "Earth_Ctrl")
#parent “Moon_Ctrl” under “Earth_Ctrl”
cmds.parent("Earth", "Earth_Ctrl")
#use setAttr command to translate Z axis of “Earth_Ctrl” to "size" * 20.0
cmds.setAttr("Earth_Ctrl.tz", size * 20.0)
#use setAttr command to translate Z axis of “Moon_Ctrl” to "size" * 3.0
# this is just to test
