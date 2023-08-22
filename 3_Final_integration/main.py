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

from drop_calc import drop_p

from roll_pitch import pitch_roll, final_dir

the_connection = mavutil.mavlink_connection('tcp:localhost:5763')
 
the_connection.wait_heartbeat()

print("Heartbeat from system (system %u component %u )" % 
      (the_connection.target_system, the_connection.target_component))






ro = 1.293  # air density
Cd = 2      # drag coefficent
A = 0.04    # reference area
m = 3       # 
g = 9.81    # gravity acceleration
L = 14      # wire length

DirectionW = 100

SpeedW = 13





################################### MESSAGES ##################################################

the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0, 74, 0, 0, 0, 0, 0, 0, 0)


def request_message_interval(message_id: int, frequency_hz: float):
    """
    Request MAVLink message in a desired frequency,
    documentation for SET_MESSAGE_INTERVAL:
        https://mavlink.io/en/messages/common.html#MAV_CMD_SET_MESSAGE_INTERVAL

    Parameters:
        message_id (int): MAVLink message ID
        frequency_hz (float): Desired frequency in Hz
    """
    the_connection.mav.command_long_send(
        the_connection.target_system, the_connection.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,
        message_id, # The MAVLink message ID
        1e6 / frequency_hz, # The interval between two messages in microseconds. Set to -1 to disable and 0 to request default rate.
        0, 0, 0, 0, # Unused parameters
        0, # Target address of message stream (if message has target address fields). 0: Flight-stack default (recommended), 1: address of requestor, 2: broadcast.
    )


#ATT! sopra 5 hz ti dava problemi 

request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_LOCAL_POSITION_NED, 5)
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_ATTITUDE, 5)
#request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_HOME_POSITION, 5)


print("\n")
print("\n")
# Set parameter value
# Set a parameter value TEMPORARILY to RAM. It will be reset to default on system reboot.
# Send the ACTION MAV_ACTION_STORAGE_WRITE to PERMANENTLY write the RAM contents to EEPROM.
# The parameter variable type is described by MAV_PARAM_TYPE in http://mavlink.org/messages/common.
the_connection.mav.param_set_send(the_connection.target_system, 
                                  the_connection.target_component,
                                  b'SIM_WIND_SPD',
                                  SpeedW,
                                  mavutil.mavlink.MAV_PARAM_TYPE_REAL32
                                 )


# hai fatto le tue prove 14 e il massimo si sono metri al secondo 



message = the_connection.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'], message['param_value']))

time.sleep(1)




the_connection.mav.param_set_send(the_connection.target_system, 
                                  the_connection.target_component,
                                  b'SIM_WIND_DIR',
                                  DirectionW,
                                  mavutil.mavlink.MAV_PARAM_TYPE_REAL32
                                 )

message = the_connection.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'], message['param_value']))

time.sleep(1)




################################### MAIN #####################################



Initial_Asset(1, 30, the_connection)

x, y, z = flyto(10, 10, 30, 0, 0, 0, 0, the_connection)

#x, y, z = drop_p(ro, Cd, A, m, g, L, R, x, y, z, the_connection)

print("\n")

# turning to the asset and check the wind 
yaw(0,-25,0,0, the_connection)




magnitude, direction = final_dir(the_connection)


print("", direction)

#x = y = z = 0

x, y, z = drop_p(ro, Cd, A, m, g, L, x, y, z, the_connection, magnitude, direction)







############################## CAME BACK 

x, y, z = flyto(0, 0, 30, 22, x, y, z, the_connection)



############################## LANDING

landing(x, y, z, the_connection)






