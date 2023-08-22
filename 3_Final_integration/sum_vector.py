#!/usr/bin/python   

'''
import matplotlib.pyplot as plt




v1 = [2,3]
v2 = [0, 5]
r = [ v1[0] + v2[0] , v1[1] + v2[1]]

origin = [0,0]

fig, ax = plt.subplots()


ax.set_xlim(-1, 5)
ax.set_ylim(-1, 10)

ax.quiver(origin[0], origin[1], v1[0], v1[1], angles='xy', scale_units='xy', scale =1, color = 'b')
ax.quiver(origin[0], origin[1], v2[0], v2[1], angles='xy', scale_units='xy', scale =1, color = 'g')
ax.quiver(origin[0], origin[1], r[0], r[1], angles='xy', scale_units='xy', scale =1, color = 'r')

plt.show()





fig, ax = plt.subplots()


ax.set_xlim(-1, 5)
ax.set_ylim(-1, 10)

ax.quiver(origin[0], origin[1], v1[0], v1[1], angles='xy', scale_units='xy', scale =1, color = 'b')
ax.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy', scale =1, color = 'g')
ax.quiver(origin[0], origin[1], r[0], r[1], angles='xy', scale_units='xy', scale =1, color = 'r')

plt.show()




def pitch_roll():
    while (True):
        try:   
            l = the_connection.recv_match().to_dict()
        
            if l['mavpackettype'] == "ATTITUDE":
             
             roll = (l['roll'] * 180) / 3.14
             pitch = (l['pitch'] * 180) / 3.14                        

            print("ROLL   PITCH ")
            print(roll, pitch)
            #cmd.append(l)
        except:
            pass
        time.sleep(0.1)








def (xf, yf, zf, xa, ya, za, the_connection):

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
                 print((xf != xi + errorx) or (yf != yi + errory))

               print("X   Y   Z (altitude))")
               print(xa, ya, -za)
               #cmd.append(l)
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
               #print("sono nell'altezza")
               print(zf)
            
               if l['mavpackettype'] == "LOCAL_POSITION_NED":
                
                 xa = int(l['x'])
                 ya = int(l['y'])
                 za = - int(l['z'])
                 print(zf != za + error, zf, za, error)

                 print("X   Y   Z (altitude))")
                 print(xa, ya, za)
                 #print((f"{(z == zi+1) or (z == zi-1)=}, {z=}, {zi=}"))
                 #print((f"{(z != zi+1) or (z != zi-1)=}, {z=}, {zi=}"))
                 #cmd.append(l)
            except:
                pass
            time.sleep(0.1)   
    return xf, yf, -zf

'''


# import the packages
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
import mpl_toolkits.axisartist.floating_axes as floating_axes

# set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# plot the figure
fig = plt.figure()

scales = (0, 5, 0, 5)



# Add 2D affine transformation
t = Affine2D().rotate_deg(90)


# Add floating axes
h = floating_axes.GridHelperCurveLinear(t, scales)
ax = floating_axes.FloatingSubplot(fig, 111, grid_helper=h)

#fig.add_subplot(ax)



plt.show()