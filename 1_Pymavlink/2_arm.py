#!/usr/bin/python
from pymavlink import mavutil
# all the commands https://ardupilot.org/copter/docs/common-mavlink-mission-command-messages-mav_cmd.html#navigation-commands


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