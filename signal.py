#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Apr 22, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: illustrative
"""

# Import modules
import FcnLibrary as fcnlib
import numpy as np
from scipy.signal import filtfilt, hamming

class UltrasonicSignal:

    UT_FILE = 'UltrasonicSignal.txt'

    def __init__(self):
        try:
            f = open(self.UT_FILE,'r')
            f.close()
        except:
            print('ERROR: COULD NOT OPEN FILE - SEE Vector.py')
                    self.readSignal()
        self.stripSignal()
        self.convertSignal()
        self.getTimeVector()
        self.smoothSignal()

    def makeParameters(self):
        axisLenStr = fcnlib.stripNewline(self.metadata[1])
        self.axisLength = self.makeFloat(axisLenStr)
        self.domainData = fcnlib.stripNewline(self.metadata[3])
        self.getDomainLimits()
        
    def getDomainLimits(self):
        Start,End,Units = self.domainData.split()
        self.step = fcnlib.getTimeStep(Start,End,self.axisLength)        
                    
    def convertSignal(self):
        for counter in range(0,len(self.signal)):
            self.signal[counter] = self.makeFloat(self.signal[counter])
            
    def makeFloat(self,arg):
        return float(arg)

    def getTimeVector(self):
        self.timeVector = fcnlib.createTime(self.step,self.axisLength)
        
    """ 
    This function uses a low-pass Hamming filter, applied to the ultrasonic signal.
    A ~100MHz bandpass (length 31) filter is used, sait seems to provide best results.
    A forward-backward smoothing algorithm is applied, via 'filtfilt'.
    """
    def smoothSignal(self):
        window = hamming(31)    
        denom = sum(window) 
        self.signalSmooth = filtfilt(window,denom,self.signal)
        
    def stripSignal(self):
        """
        Each line from the signal '.txt' file has an endline character.
        This funciton is used to strip that enline character.
        The next function after that allows conversion to float type data.
        """
        for counter in range(0,len(self.signal)):
            self.signal[counter] = fcnlib.stripNewline(self.signal[counter])        
        
    def readSignal(self):         
        """
        This function is used to get the ultrasonic data from a 'txt' file
        The file is always of the same arrangement.
        The first 7 lines are metadata on the signal.
        The next lines are signal data.
        """     
        self.metadata = np.array([])
        with open(self.UT_FILE,'r') as file:
            for lines in range(0,7):
                self.metadata = np.append(self.metadata,file.readline())
            self.makeParameters()
            self.signal = np.empty(int(self.axisLength),dtype=object)
            counter = 0
            for f in file:
                self.signal[counter] = f
                counter += 1
