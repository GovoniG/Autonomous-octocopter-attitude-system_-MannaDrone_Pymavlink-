#!/usr/bin/python   
from pymavlink import mavutil
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import pyplot
import pandas as pd
import numpy as np
from numpy import arctan
import time
import random
import math
from math import asin, atan2, cos, degrees, radians, sin
import itertools


def pitch_roll(the_connection):
    f = 0
    while (f != 100):
        try:   
            l = the_connection.recv_match().to_dict()
        
            if l['mavpackettype'] == "ATTITUDE":
             
              roll = (l['roll'] * 180) / 3.14
              pitch = (l['pitch'] * 180) / 3.14   
              f = f + 1                     

              print("    ROLL                PITCH ")
              print(roll, pitch)

        except:
            pass
        time.sleep(0.1)

    return roll, pitch


def final_dir(the_connection):

     roll, pitch = pitch_roll(the_connection)

     # u know the maximum and the minimum 

     v1 = [0,0]
     v2 = [0,0]

     v1[0] = abs(pitch) * (14/28)
     v2[0] = abs(roll) * (14/28)

     if (pitch > 0):
         v1[1] = 180
     else:v1[1] = 0
    
     if (roll > 0):
         v2[1] = 90
     else:v2[1] = 270


     vx1 = v1[0] * (np.cos((v1[1])*3.14/180))
     vy1 = v1[0] * (np.sin((v1[1])*3.14/180))
     
     vx2 = v2[0] * (np.cos((v2[1])*3.14/180))
     vy2 = v2[0] * (np.sin((v2[1])*3.14/180))
   

     print("vx1", vx1)
     print("vy1", vy1)

     print("vx2", vx2)
     print("vy2", vy2)



     print('modulo1',v1[0])
     print('direzione1',v1[1])
     print('modulo2',v2[0])
     print('direzione2',v2[1])


     print('coordinate1',vx1,vy1)
     print('coordinate2',vx2,vy2)


     origin = [0,0]

     fig, ax = plt.subplots()
     

     ax.set_xlim( -17, 17)
     ax.set_ylim( -17, 17)

     r = [vx1 + vx2 , vy1 + vy2]
     print('r', r)

     q = 0
     if (r[1] < 0):
            q = 3

     t1 = ax.quiver(origin[0], origin[1], vx1, vy1, angles='xy', scale_units='xy', scale =1,color = 'b' )
     t2 = ax.quiver(origin[0], origin[1], vx2, vy2, angles='xy', scale_units='xy', scale =1, color = 'g')
     t3 = ax.quiver(origin[0], origin[1], r[0], r[1], angles='xy', scale_units='xy', scale =1, color = 'r')

     ax.legend(r)
     plt.legend([t1, t2, t3], ['Pitch_direction', 'Roll_direction', 'Wind_direction'])

     plt.grid()
     plt.show()
    


     magnitude = math.sqrt((r[0])**2 + (r[1])**2)

     print('magnitude',magnitude)

     direction = r[0]/magnitude
     print('direction',direction)
     p = np.arccos((direction))
     print('direction',p)
     s = p*180/3.14
     print("q value", q)
     if(q == 3 or q == 4):
         s = 360 - s
     print('direction',s)
   
     print("\n")
     print("cambio in coordinate di pymavlink")
     print("\n")

     f = 90 - s

     print(f)

     if (f < 0):
       l = 360 + f
       direction = l
     else: direction = f
     
     return magnitude, direction


