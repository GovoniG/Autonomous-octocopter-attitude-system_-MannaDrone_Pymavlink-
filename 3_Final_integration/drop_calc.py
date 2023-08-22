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




def drageq(ro, v, Cd, A):
    """
    Drag equation implementation

    Parameters
    ----------
    ro:(int) air density
    v: (int) wind velocity
    Cd:(int) drag coefficent
    A: (int) Area
    
    OUT
    Fw: (int) wind force
    """

    Fw = (ro * (v**2) * Cd * A)/2
    return Fw


def delivery(xf, yf, zf, dir, xa, ya, za, the_connection):
    """
    Simulates the timing of a drone delivery, 
    calling up the adjust function to drop down to 10 m
    Also adjust the new setup for the delivery.

    """
   
    print("\n")
    print("\n")
    print("                   #####  DELIVERY IN PROGRESS  #####") 
    print("\n")
    print("                     SET 10 METERS TO THE GROUND ")
    Animation_MoveDown_Drone()
    time.sleep(5)


    x, y, z = flyto(xa, ya, 10, 0, xa, ya, za, the_connection)

    Animation_Package_Drone()
    time.sleep(5)
    Animation_PackageWIND_Drone()

    print("\n")
    print("\n")
    print("                   #####  DELIVERY ADJUSTMENT  #####") 
    print("\n")
    print("                   SETTING NEW POSITION AND ALTITUDE ")
    Animation_PackageAdjust_Drone()



    print("Final cordinates")
    print("X  ",xf, "m")
    print("Y  ",yf, "m")

    print('Setting new position')
    x, y, z = flyto(xf, yf, 10, 0, x, y, z, the_connection)
  
    print('Setting new altitude')
    x, y, z = flyto(xf, yf, zf, dir, x, y, z, the_connection)
  

    print("\n")
    print("\n")
    print("                   #####  DROPPING PACKAGE  #####") 
    print("\n")
    print("\n")

    time.sleep(20)

    print("\n")
    print("\n")
    print("                   #####  DELIVERY EFFECTED  #####") 
    print("\n")
    print("\n")

    print('Asset to flight back')
    x, y, z = flyto(xf, yf, 30, 22, x, y, z, the_connection)

    return x,y,z



def setAdjust(Fw ,Fg, L):

     rap = Fw/Fg
     print("Fw/Fg=", rap)
     tang = math.tan(Fw/Fg)
     print("tang", tang)
     gamma = arctan(tang)
     print("gamma", gamma)


     print("\n")
     print("                   #####  NEW VALUES  #####")
     print("\n")
     print("math.sin(gamma)",math.sin(gamma))
     dist = L * (math.sin(gamma))


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
     newalt = round(newalt, 1)
     print("new altitude", newalt, "m")
     print("\n")

     return newalt, dist





def drop_p(ro, Cd, A, m, g, L, x, y, z, the_connection, windV, dir):

    print("\n")

    Fw = drageq(ro, windV, Cd, A)
    Fg = m * g

    print("wind force", Fw, "N")
    print("\n")
    print("la direzione", dir)

    ############################### NEW ALTITUDE AND DISTANCE

    newalt, dist = setAdjust(Fw, Fg, L)

    ############################## SET NEW POSITION

    print("\n")
    print("\n")
    print("\n")
    print("\n")

    print("distance", dist)
    print("\n")
    print("\n")

    print("coseno", (math.cos((dir)*3.14/180)))
    print("\n")
    print("\n")
    print("seno", (math.sin((dir)*3.14/180)))

    print("\n")
    print("\n")
    print("direzione", dir)

    xo = dist * (math.cos((dir)*3.14/180))
    yo = dist * (math.sin((dir)*3.14/180))

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



