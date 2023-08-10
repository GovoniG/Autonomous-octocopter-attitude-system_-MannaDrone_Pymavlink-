#!/usr/bin/python  
from pymavlink import mavutil
import time


# Start a connection listening on a UDP port
# using the function mavlink_connection
the_connection = mavutil.mavlink_connection('tcp:localhost:5763')

# Wait for the first heartbeat {}
# the aircraft is sending constantly heartbeat 
# here is wait for the first heartbeat to proceed in the code
the_connection.wait_heartbeat()

print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))


# Sending the command MAV_CMD_COMPONENT_ARM_DISARM
# for the second parameter
# 1 --> ARM
# 0 --> DISARM
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)

msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)


# define the type of mode
mode = 'GUIDED'
mode_id = the_connection.mode_mapping()[mode]

# Sending the move_id through the connection
the_connection.mav.set_mode_send(the_connection.target_system,mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,mode_id)

msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)


#Sending the command MAV_CMD_NAV_TAKEOFF
# the last parameter determines the height that is reached with the take_off
the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 2, 0, 0, 0, 0, 0, 0, 10)

msg = the_connection.recv_match(type='COMMAND_ACK', blocking=True)
print(msg)




#Sending the command MAV_CMD_CONDITION_YAW
# param 0   ////////////////////////
# param 1   target as angle
# param 2   speed rotation (degree/sec)
# param 3   which direction the speed 1 anticlockwise
# param 4   0 absolute orientation    1 rekative orientation

the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                     mavutil.mavlink.MAV_CMD_CONDITION_YAW, 0, 45, 25, 0, 0, 0, 0, 0)



#Sending the command MAV_CMD_DO_CHANGE_SPEED
# param 0   ////////////////////////
# param 1   Speed type (0,1=Ground Speed, 2=Climb Speed, 3=Descent Speed)
# param 2   Target speed (m/s)

the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                    mavutil.mavlink.MAV_CMD_DO_CHANGE_SPEED, 0, 10, 0, 0, 0, 0, 0, 0)




