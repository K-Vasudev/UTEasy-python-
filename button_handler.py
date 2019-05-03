#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Mar 26, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: illustrative
"""

# Import modules
import numpy as np

"""
This class holds all the actions taken by button objects
"""
class ButtonObject:

    # Initialization of class, gets signalHandler object
    def __init__(self,signalHandler):
        self.signalTarget = signalHandler

    # Controls for the 'toggle peaks' button
    def togglePeaks(self,event):
        print('Toggle')
    
    # Controls for the 'smooth signal' button
    def toggleSmoothing(self,event):
        print('Smooth') 
