#!/usr/bin/python
from pymavlink import mavutil
# all the commands https://ardupilot.org/copter/docs/common-mavlink-mission-command-messages-mav_cmd.html#navigation-commands

# Start a connection listening on a UDP port
# using the function mavlink_connection
the_connection = mavutil.mavlink_connection('tcp:localhost:5763')


# Wait for the first heartbeat {}
# The aircraft is sending constantly heartbeat 
# here is wait for the first heartbeat to proceed in the code
the_connection.wait_heartbeat()

print("Heartbeat from system (system %u component %u)" % 
      (the_connection.target_system, the_connection.target_component))


# Once connected, use 'the_connection' to get and send messages
while 1:
    msg = the_connection.recv_match(blocking=True)          
    print(msg)
