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
import fcnLibrary as fcnlib
from scipy.signal import filtfilt, hamming


class SignalHandler:

    def __init__(self,ax):
        self.signalObj = UltrasonicSignal()
        self.axis = ax
        self.signal = self.signalObj.signal
        self.smoothSignal = self.signalObj.smoothSignal
        self.timeVector = self.signalObj.timeVector
       
    def findSignalPeaks(self):
        self.signalPeaks = fcnlib.findPeaks(self.signalObj.signal,self.THRESH,self.DEC)
        
    def plotLines(self):
        self.axis.plot(self.timeVector,self.signal)
    
    def setAxis(self,ax):
        self.axis = ax
        
    def getAxis(self):
        return self.axis
        
    def getPlotXLim(self):
        pass
        
    def getPlotYLim(self):
        pass

class PeakHandler:
    THRESH = 0.5
    DEC = 0.2

    def __init__(self,FTAxes):
        print("Peak handler created")
        self.axis = FTAxes
        
    def findSignalPeaks(self):
        self.signalPeaks = fcnlib.findPeaks(self.signalObj.signal,self.THRESH,self.DEC)        
        
class FTHandler:

    def __init__(self):
        print("FT Handler created")
        
"""
In this module:

Classes:
    SignalHandler
        Methods:
        Properties:
            signalObj
            signal
            smoothSignal
            timeVector
            axis
            line(?)
    PeakHandler
        Methods:
        Properties:
            THRESH (global)
            DEC (global)  
            axis
            signalHandler
            peakVoltages
            peakTimes
            
    FTHandler
        Methods:
        Properties:
"""   
