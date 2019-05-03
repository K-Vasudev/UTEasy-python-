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

    def __init__(self,signalHandler):
        self.signalTarget = signalHandler

    def togglePeaks(self,event):
        print('Toggle')
        
    def toggleSmoothing(self,event):
        print('Smooth') 
