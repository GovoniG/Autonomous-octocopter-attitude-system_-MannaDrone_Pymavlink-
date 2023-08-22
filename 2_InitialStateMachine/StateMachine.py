#!/usr/bin/python   
from pymavlink import mavutil
import matplotlib.pyplot as plt
import pandas as pd
import time



xi = yi = zi = 0
cmd = []

the_connection = mavutil.mavlink_connection('tcp:localhost:5763')
 
the_connection.wait_heartbeat()

print("Heartbeat from system (system %u component %u )" % 
      (the_connection.target_system, the_connection.target_component))

the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component, mavutil.mavlink.MAV_CMD_REQUEST_MESSAGE, 0, 74, 0, 0, 0, 0, 0, 0, 0)




def request_message_interval(message_id: int, frequency_hz: float):
    """
    Request MAVLink message in a desired frequency,
    documentation for SET_MESSAGE_INTERVAL:
        https://mavlink.io/en/messages/common.html#MAV_CMD_SET_MESSAGE_INTERVAL

    Args:
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



request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_LOCAL_POSITION_NED, 1)




# FUNCTIONS

def arrive_q(x, y, z, xi, yi, zi):
    """
    Captures messages that are covered in the dictionary.
    Filters telemetry data from LOCAL_POSITION_NED.
    Calculates incremental and decremental position error.

    Parameters
    ----------
    x, y, z    (int) : required position value 
    xi, yi, zi (int) : current position value
    OUT
    current position values
    """
    if(x>xi or y>yi or z>zi):
          error = 1
    else: error = -1

    while (((xi!=x) or (x!=xi+error)) and ((yi!=y) and (y!=yi+error)) and ((zi!=-z) or (z!=-zi-error))):
        try:
            l = the_connection.recv_match().to_dict()
        
            if l['mavpackettype'] == "LOCAL_POSITION_NED":
             
             xi = int(l['x'])
             yi = int(l['y'])
             zi = int(l['z'])

             print("X   Y   Z (altitude))")
             print(xi, yi, -zi)
             cmd.append(l)
        except:
          pass
          time.sleep(0.1)
    return xi, yi, -zi



def flyto(x, y, z, xi, yi, zi):
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
                                                                                      int(0b110111111000), x, y, -z, 0, 0, 0, 
                                                                                      0, 0, 0, 0, 0))
    xi, yi, zi = arrive_q(x, y, z, xi, yi, zi)
    return xi, yi, zi



def Arm(a):
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



def Guided_mode():
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




def Take_off(altitude):
     """
     sets the altitude for take-off and executes it 
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
     time.sleep(20) 



def Initial_Asset(a, altitude):
    """
    set of procedures required 
    for initial set-up

    Parameters
    ----------
    a:        (int) arm or disarm motor selection
    altitude: (int)
    """
    print("\n")
    print("\n")
    print("                   #####  START DELIVERY  #####")
    print("\n")
    print("\n")
    Arm(a)
    Guided_mode()
    Take_off(altitude)



def delivery(xd, yd, zd):
     """
     Simulates the timing of a drone delivery, 
     calling up the flyto function to drop down to 10 m

     Parameters
     ----------
     xd: (int), current positions 
     yd: (int)
     zd: (int)
     """
     x, y, z = flyto(xd,yd,10,xi,yi,zi)
     i = 0
     while(i != 5):
         time.sleep(5)
         i = i + 1
         print("\n")
         print("\n")
         print("                   #####  DELIVERY IN PROGRESS  #####") 
         print("\n")
         print("\n")

     print("\n")
     print("\n")
     print("                   #####  DELIVERY EFFECTED  #####") 
     print("\n")
     print("\n")
     flyto(x,y,30,xi,yi,zi)
     time.sleep(10)


def landing(xi, yi, zi):
    """
    Call up the flyto function to return to the 
    starting position at an altitude of 0m, 
    on the way also return to the 0 degree position 
    via the yaw function

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

    xi,yi,zi = flyto(0,0,0,xi,yi,zi)
    time.sleep(10)

    yaw(0,-25,0,0)

    time.sleep(2)

    print("\n")
    print("\n")
    print("                   #####  LANDED  #####")

    Arm(0)




def yaw(ang,vel,dir,abs):
    the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                      mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0, ang, vel, dir, abs, 0, 0, 0)
    time.sleep(10)








                                  #####     MAIN STATE MACHINE    #####


# STATE 1 
Initial_Asset(1, 30)

# STATE 2
xi,yi,zi = flyto(300,300,30,xi,yi,zi)

#STATE 3
delivery(xi, yi, zi)

# STATE 4
xi,yi,zi = flyto(0,0,30,xi,yi,zi)

# STATE 5
landing(xi, yi, zi)
time.sleep(10)

# STATE 6
Arm(1)
xi,yi,zi = flyto(0,0,30,xi,yi,zi)
time.sleep(10)

# STATE 7
xi,yi,zi = flyto(300,-300,30,xi,yi,zi)

# STATE 8
delivery(xi, yi, zi)

# STATE 9
xi,yi,zi = flyto(0,0,30,xi,yi,zi)

# STATE 10
landing(xi, yi, zi)

