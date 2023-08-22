#!/usr/bin/python   
from pymavlink import mavutil
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy import arctan
import time
import random
import math
from math import asin, atan2, cos, degrees, radians, sin


from Drawings import Animation_Initial_Drone, Animation_TakeOFF_Drone, Animation_MoveUp_Drone, Animation_MoveDown_Drone, Animation_PackageWIND_Drone, Animation_Package_Drone, Animation_PackageAdjust_Drone

from Movement import arrive_q, flyto, landing, yaw

from Initial import Initial_Asset, Guided_mode, Take_off


the_connection = mavutil.mavlink_connection('tcp:localhost:5763')
 
the_connection.wait_heartbeat()

print("Heartbeat from system (system %u component %u )" % 
      (the_connection.target_system, the_connection.target_component))




#Initial_Asset(1, 30, the_connection)


'''


def setAdjust(Fw ,Fg, L):

     #tang = (np.tan(np.radians(Fw/Fg)))*180/3.14
     tang = math.tan(Fw/Fg)
     #gamma = (np.arctan(np.radians(tang)))*180/3.14
     gamma = arctan(tang)
     #tanb = (np.tan(np.radians(Fg/Fw)))*180/3.14
     tanb = math.tan(Fg/Fw)
     #beta = (np.arctan(np.radians(tanb)))*180/3.14
     beta = arctan(tanb)

     print("\n")
     print("                   #####  NEW VALUES  #####")
     print("\n")
     #dist = L * (np.sin(np.radians(gamma)))*180/3.14
     dist = L * (math.sin(gamma))
     #dist = int(dist)
     dist = round(dist, 1)
     print("SET NEW ABSOLUTE DISTANZE =  ", dist, "m")
     print("\n")
    
     if (dist > 3):
         error = dist - 3
         dist = 3

         print("\n")
         print("                  ##### ATTENTION ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("                  ##### ATTENTION ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("            ##### DISTANCE LIMIT EXCEEDED ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("               ##### NEW SET DISTANCE #####    ===>  3 m ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("               ##### ERROR OF : #####    ===>  ", error)
         print("\n")



     #newalt = L * (np.cos(np.radians(gamma)))*180/3.14
     newalt = L * (math.cos(gamma))
     #newalt = int(newalt)
     newalt = round(newalt, 1)
     print("new altitude", newalt, "m")
     print("\n")

     return newalt, dist





def setvecchio(Fw ,Fg, L):
     tang = math.tan(Fw/Fg)
     gamma = arctan(tang)

     tanb = math.tan(Fg/Fw)
     beta = arctan(tanb)

     print("\n")
     print("                   #####  NEW VALUES  #####")
     print("\n")
     dist = L * (math.sin(gamma))
     #dist = int(dist)
     dist = round(dist, 1)
     print("SET NEW ABSOLUTE DISTANZE =  ", dist, "m")
     print("\n")
    
     if (dist > 3):
         error = dist - 3
         dist = 3

         print("\n")
         print("                  ##### ATTENTION ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("                  ##### ATTENTION ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("            ##### DISTANCE LIMIT EXCEEDED ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("               ##### NEW SET DISTANCE #####    ===>  3 m ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("               ##### ERROR OF : #####    ===>  ", error)
         print("\n")

     newalt = L * (math.cos(gamma))
     #newalt = int(newalt)
     newalt = round(newalt, 1)
     print("new altitude", newalt, "m")
     print("\n")

     return newalt, dist



# att perche ovviamente la forza gravitazionale e 9.81 per la massa 

newalt,dist = setAdjust(10,29.43,10)


newalt,dist = setvecchio(10,29.43,10)


'''

'''
#p = math.cos(90)
p = (np.cos(180*3.14/180))
print(p)   





c = (np.sin(180*3.14/180))

#c = math.sin(90)     
print(c)  

'''
#x = 5
#y = 4

#magnitude = 6.4


#direction = (np.arccos(((90)*3.14/180)))
#print('direction',direction)


#p2 = math.acos(1.57)

#print(p2)

#l = ((90)*3.14/180)
#print(l)



#c = np.arcsin(90*3.14/180)
#print(c)

'''

def drageq(ro, v, Cd, A):
    Fw = (ro * (v**2) * Cd * A)/2
    return Fw




def setAdjust(Fw ,Fg, L):

     #tang = (np.tan(np.radians(Fw/Fg)))*180/3.14
     rap = Fw/Fg
     print("Fw/Fg=", rap)
     tang = math.tan(Fw/Fg)
     print("tang", tang)
     #gamma = (np.arctan(np.radians(tang)))*180/3.14
     gamma = arctan(tang)
     print("gamma", gamma)
     #tanb = (np.tan(np.radians(Fg/Fw)))*180/3.14
     
     print("\n")
     print("\n")
     print("TESTTTTTTTT")
     print("\n")
     print("\n")



     t = np.tan(math.radians(0))
     print(t)
     t = np.tan(math.radians(90))
     print(t)
     t = np.tan(math.radians(180))
     print(t)
     t = np.tan(math.radians(270))
     print(t)



     print("\n")
     t = np.tan(0)
     print(t)
     t = np.tan(90)
     print(t)
     t = np.tan(180)
     print(t)
     t = np.tan(270)
     print(t)


     print("\n")
     print("                   #####  NEW VALUES  #####")
     print("\n")
     #dist = L * (np.sin(np.radians(gamma)))*180/3.14
     print("math.sin(gamma)",math.sin(gamma))
     dist = L * (math.sin(gamma))


     #dist = int(dist)
     dist = round(dist, 1)
     print("SET NEW ABSOLUTE DISTANZE =  ", dist, "m")
     print("\n")
    
     if (dist > 3):
         error = dist - 3
         dist = 3

         print("\n")
         print("                  ##### ATTENTION ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("                  ##### ATTENTION ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("            ##### DISTANCE LIMIT EXCEEDED ##### ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("               ##### NEW SET DISTANCE #####    ===>  3 m ")
         print("\n")

         time.sleep(1)

         print("\n")
         print("               ##### ERROR OF : #####    ===>  ", error)
         print("\n")



     #newalt = L * (np.cos(np.radians(gamma)))*180/3.14
     newalt = L * (math.cos(gamma))
     #newalt = int(newalt)
     newalt = round(newalt, 1)
     print("new altitude", newalt, "m")
     print("\n")

     return newalt, dist


def drop_p(ro, Cd, A, m, g, L, R, x, y, z, the_connection, windV, dir):

    print("\n")

    Fw = drageq(ro, windV, Cd, A)
    Fg = m * g

    print("wind force", Fw, "N")
    print("\n")
    print("la direzione", dir)

    ############################### NEW ALTITUDE AND DISTANCE

    newalt, dist = setAdjust(Fw, Fg, L)

    ############################## SET NEW POSITION

    #newalt = L * (math.cos(gamma))
    #xo = dist*(np.cos(np.radians(dir)))* 180 / 3.14

    xo = dist * (math.cos((dir)*3.14/180))
    yo = dist * (math.sin((dir)*3.14/180))
    #yo = round(dist*(np.sin(np.radians(dir)))* 180 / 3.14)

    print("\n")
    print("\n")
    print("coordinate calcolate",xo, yo)
    print("\n")
    print("\n")

    xf = xo + x
    yf = yo + y 

    print("Final cordinates")
    print("X  ",xf, "m")
    print("Y  ",yf, "m")

    return x, y, z



ro = 1.293  # air density
Cd = 2      # drag coefficent
A = 0.04    # reference area
m = 3       # 
g = 9.81    # gravity acceleration
L = 10      # wire length
R = 6371    # radius of sphere



x = y = z = 0


magnitude = 12.8

direction = 180



x, y, z = drop_p(ro, Cd, A, m, g, L, R, x, y, z, the_connection, magnitude, direction)


'''



g = 270

f = 90 - g

print(f)

if (f < 0):
    l = 360 + f

print(l)

