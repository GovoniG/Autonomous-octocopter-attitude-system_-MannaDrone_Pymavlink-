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

from Movement import arrive_q, flyto, landing, yaw, Arm

 

################################### MESSAGES ##################################################

#the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0, 74, 0, 0, 0, 0, 0, 0, 0)

def Guided_mode(the_connection):            
    """
    Set the GUIDE mode via the command 
    MAV_MODE_FLAG_CUSTOM_MODE_ENABLED.

    """ 
    mode = 'GUIDED'
    mode_id = the_connection.mode_mapping()[mode]

    the_connection.mav.set_mode_send(the_connection.target_system,mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,mode_id)

    print("\n")
    print("                   #####  GUIDE MODE  #####")
    print("\n")
    msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)



def Take_off(altitude, the_connection):   
    """
    Sets the altitude for take-off and executes it 
    via the MAV_CMD_NAV_TAKEOFF command

    Parameters
    ----------
    altitude: (int)
    """
    the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 2, 0, 0, 0, 0, 0, 0, altitude)
    
    print("\n")
    print("                   #####  TAKE OFF  #####")
    print("\n")
    msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
    print(msg)

    arrive_q(0, 0, altitude, 0, 0, 0, the_connection)

    Animation_TakeOFF_Drone()

    #time.sleep(20) 


def Initial_Asset(a, altitude, the_connection):   
    """
    set of procedures required 
    for initial set-up

    Parameters
    ----------
    a:(int) arm or disarm motor selection
    altitude: (int)
    """
    print("\n")
    print("\n")
    print("                   #####  START DELIVERY  #####")

    Animation_Initial_Drone()

    Arm(a, the_connection)
    Guided_mode(the_connection)
    Take_off(altitude, the_connection)
    print("penultimo stadio")



#Initial_Asset(1, 30) 