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



def Arm(a, the_connection):
    """
    Arms the drone motor via the
    command MAV_CMD_COMPONENT_ARM_DISARM.

    Parameters
    ----------
    a: (int), 1 --> arm
              0 --> disarm
    """
    the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, a, 0, 0, 0, 0, 0, 0)

    print("\n")
    if(a == 1):
       print("                   #####  MOTOR ARM  #####")
    else: print("                   #####  MOTOR DISARM  #####")
    print("\n")
    msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)



def arrive_q(xf, yf, zf, xa, ya, za, the_connection):

    #if(x>xi or y>yi or z>zi):
    #error = 1
    #else: error = -1
    
    if(xf != xa or yf != ya):
        if(xf<xa):
          errorx = -1
        else: errorx = 1
        if(yf<ya):
          errory = -1
        else: errory = 1
        while (((xf!=xa) and (xf != xa + errorx)) and ((yf!=ya) and (yf != ya + errory))):
            try:   
               l = the_connection.recv_match().to_dict()
        
               if l['mavpackettype'] == "LOCAL_POSITION_NED":
             
                 xa = int(l['x'])
                 ya = int(l['y'])
                 za = int(l['z'])

               print("X   Y   Z (altitude))")
               print(xa, ya, -za)
            except:
                pass
            time.sleep(0.1)

    if(zf!=za):
        if(zf<za):
          error = -1
        else: error = 1

        while (((zf!=za) and (zf != za + error))):
            try:  
               l = the_connection.recv_match().to_dict()
            
               if l['mavpackettype'] == "LOCAL_POSITION_NED":
                
                 xa = int(l['x'])
                 ya = int(l['y'])
                 za = - int(l['z'])

                 print("X   Y   Z (altitude))")
                 print(xa, ya, za)
            except:
                pass
            time.sleep(0.1)   
    return xf, yf, -zf


def flyto(xf, yf, zf, dir, xa, ya, za, the_connection):
 
     """
     Set a target position for the aircraft with the
     MAVLink_set_position_target_local_ned_messag 
     command, passing the data to the arrive_q function 
     for telemetry.

     Parameters
     ----------
     x, y, z    (int) : required position value 
     xi, yi, zi (int) : current position value
     OUT
     current position values
     """
     the_connection.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, the_connection.target_system, 
                                                                                      the_connection.target_component, 
                                                                                      mavutil.mavlink.MAV_FRAME_LOCAL_NED, 
                                                                                      int(0b110111111000), xf, yf, -zf, 0, 0, 0, 
                                                                                      0, 0, 0, dir, 0))
     print("im going to", xf, yf, zf)


     xa, ya, za = arrive_q(xf, yf, zf, xa, ya, za, the_connection)
     time.sleep(10)
     return xa, ya, -za



def landing(x, y, z, the_connection):
    """
    Include steps for landing the drone 
    to return to its initial position.
    Throght the adjust and yaw function  
    the drone came back to the home position
    and in the correct orientation.
    At the end the drone is disarm.

    Parameters
    ----------
    xi: (int), current positions 
    yi: (int)
    zi: (int)
    """
    print("\n")
    print("\n")
    print("                   #####  LANDING  #####")
    print("\n")
    print("\n")

    x, y, z = flyto(0, 0, 0, 0.0, x, y, z, the_connection)
    
    yaw(0,-25,0,0, the_connection)

    time.sleep(2)

    print("\n")
    print("\n")
    print("                   #####  LANDED  #####")

    Arm(0, the_connection)



def yaw(ang,vel,dir,abs,the_connection):
    """
    Include the function to effect the YAW

    Parameters
    ----------
      parma 0 ()  ////////////////////////
      param 1 (ang) il target come angolo
      param 2 (vel) speed rotation (degree/sec)
      param 3 (dir) which direction the speed 1 anticlockwise
      param 4 (abs) 0 absolute orientation    1 rekative orientation

    """
    the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                      mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0, ang, vel, dir, abs, 0, 0, 0)
    time.sleep(15)
