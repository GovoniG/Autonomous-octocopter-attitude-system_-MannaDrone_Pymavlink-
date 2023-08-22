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





def Animation_Initial_Drone():

   print("                                                    #             #")
   print("                                                  #   #         #   #")
   print("                                                    #             #")
   print("                                                    #   #######   #")
   print("                                                    ###############")
   print("                                                        #######  ")
   print("                                                        _______          HOME   ")


   print("\n")

def Animation_TakeOFF_Drone():
    print("\n")
    print("\n")
    print("\n")



    print("                                                    #             #")
    print("                                                  #   #         #   #")
    print("                                                    #             #")
    print("                                                    #   #######   #")
    print("                                                    ###############")
    print("                                                        #######  ")
    print("                                                                          _  ")
    print("                                                                            ")
    print("                                                                          |  ")
    print("                                                          /\              |  ")
    print("                                                         /  \             |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                                          |  ")
    print("                                                                          |  ")
    print("                                                                          _  ")

    print("\n")

    print("                                                        _______          HOME   ")

    print("\n")



def Animation_MoveUp_Drone():
    print("\n")
    print("\n")
    print("\n")



    print("                                                    #             #")
    print("                                                  #   #         #   #")
    print("                                                    #             #")
    print("                                                    #   #######   #")
    print("                                                    ###############")
    print("                                                        #######  ")
    print("                                                                          _  ")
    print("                                                                            ")
    print("                                                                          |  ")
    print("                                                          /\              |  ")
    print("                                                         /  \             |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                                          |  ")
    print("                                                                          |  ")
    print("                                                                          _  ")


    print("\n")
    print("\n")
    print("\n")



def Animation_MoveDown_Drone():
    print("\n")
    print("\n")
    print("\n")



    print("                                                    #             #")
    print("                                                  #   #         #   #")
    print("                                                    #             #")
    print("                                                    #   #######   #")
    print("                                                    ###############")
    print("                                                        #######  ")
    print("                                                                          _  ")
    print("                                                                            ")
    print("                                                                          |  ")
    print("                                                                          |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                          ||              |  ")
    print("                                                         \  /             |  ")
    print("                                                          \/              |  ")
    print("                                                                          |  ")
    print("                                                                          |  ")
    print("                                                                          _  ")


    print("\n")
    print("\n")
    print("\n")


def Animation_PackageWIND_Drone():
    print("\n")
    print("\n")
    print("\n")


    print("                     WIND                           #             #")
    print("                         --->                     #   #         #   #")
    print("                         --->                       #             #")
    print("                         --->                       #   #######   #")
    print("                                                    ###############")
    print("                                                        #######  ")
    print("                                                           #  ")
    print("                                                               ")
    print("                                                             #  ")
    print("                                                                ")
    print("                                                               #  ")
    print("                                                                  ")
    print("                                                                 #  ")
    print("                                                                   ")
    print("                                                                   #  ")
    print("                                                                      ")
    print("                                                                     #  ")
    print("                                                                     ")
    print("                                                                       #  ")
    print("                                                                          ")
    print("                                                                         #  ")
    print("                                                                            ")
    print("                                                                           #  ")
    print("                                                                                   ")
    print("                                                                             #  ")
    print("                                                                                ")
    print("                                                                               #  ")
    print("                                                                             #####  ")
    print("                                                                             #####  ")
    print("                                                                             #####  ")
    print("\n")
    print("                                                         _____   TARGET   ")



    print("\n")
    print("\n")
    print("\n")



def Animation_Package_Drone():
    print("\n")
    print("\n")
    print("\n")


    print("                                                    #             #")
    print("                                                  #   #         #   #")
    print("                                                    #             #")
    print("                                                    #   #######   #")
    print("                                                    ###############")
    print("                                                        #######  ")
    print("                                                           #  ")
    print("                                                             ")
    print("                                                           #  ")
    print("                                                             ")
    print("                                                           #  ")
    print("                                                             ")
    print("                                                           #  ")
    print("                                                             ")
    print("                                                           #  ")
    print("                                                             ")
    print("                                                           #  ")
    print("                                                            ")
    print("                                                           #  ")
    print("                                                            ")
    print("                                                           #  ")
    print("                                                            ")
    print("                                                           #  ")
    print("                                                            ")
    print("                                                           #  ")
    print("                                                            ")
    print("                                                           #  ")
    print("                                                         #####  ")
    print("                                                         #####  ")
    print("                                                         #####  ")
    print("\n")
    print("                                                         _____   TARGET   ")

    print("\n")
    print("\n")
    print("\n")


def Animation_PackageAdjust_Drone():
    print(" WIND                           #             #")
    print("     --->                     #   #         #   #         <=========== ")
    print("     --->                       #             #           <=========== ")
    print("     --->                       #   #######   #           <=========== ")
    print("                                ###############")
    print("                                    #######  ")
    print("                                       #  ")
    print("                                                               ")
    print("                                         #  ")
    print("                                                         ")
    print("                                           #  ")
    print("                                                                  ")
    print("                                             #  ")
    print("                                                       ")
    print("                                               #  ")
    print("                                                                      ")
    print("                                                 #  ")
    print("                                                                 ")
    print("                                                   #  ")
    print("                                                                          ")
    print("                                                     #  ")
    print("                                                                     ")
    print("                                                       #  ")
    print("                                                                      ")
    print("                                                         #  ")
    print("                                                                           ")
    print("                                                           #  ")
    print("                                                         #####  ")
    print("                                                         #####  ")
    print("                                                         #####  ")
    print("\n")
    print("                                                         _____   TARGET   ")