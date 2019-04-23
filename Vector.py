#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Mar 26, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: illustrative
"""

import numpy as np
import FcnLibrary as fcnlib
from scipy.signal import filtfilt, hamming

class createVector:
                                            # UltrasonicSignal is *Grade 483,S3,C1, Longitudinal data #1
    UT_FILE = 'UltrasonicSignal.txt'        # Filename of ultrasonic data 
    THRESH = 0.5                            # Starting threshold for peak detection
    DEC = 0.2                               # Decrease rate of threshold
    
    """
    Initialization (on creation) behavior of 'createVector' class.
    Check to see if the file specified above ('UT_FILE') can be accessed.
    """
    def __init__(self):                                         # Behavior on creation
        try:
            f = open(self.UT_FILE,'r')                          # Check to see if UT_FILE is available
            f.close()                                           # Won't use UT_FILE yet
        except:
            print('ERROR: COULD NOT OPEN FILE - SEE Vector.py')        # Print error message
        
    """
    This function is used to get the ultrasonic data from a 'txt' file
    The file is always of the same arrangement.
    The first 7 lines are metadata on the signal.
    The next lines are signal data lines.
    """
    def readUltrasonic(self):       
        self.metadata = np.array([])            # Preallocated for metadata
        with open(self.UT_FILE,'r') as file:
            for lines in range(0,7):
                self.metadata = np.append(self.metadata,file.readline())
            self.getParameters()                                            # Get axis length and domain
            self.signal = np.empty(int(self.axisLength),dtype=object)       # Signal preallocation
            counter = 0
            for f in file:                      # Iterate through remaining lines
                self.signal[counter] = f        # 'f' holds the actual line in this way
                counter += 1
                
    def getParameters(self):
        self.axisLength = fcnlib.stripNewline(self.metadata[1])     # Get axis length
        self.domain = fcnlib.stripNewline(self.metadata[3])         # Get signal domain (time)
        self.getDomain()                                            # Call 'getDomain' to extract domain    
        
    def getDomain(self):                                            # Used to extract domain
        Start,End,Units = self.domain.split()
        self.step = fcnlib.getTimeStep(Start,End,self.axisLength)   # Call 'getTimeStep'
        
        
    """
    Each line from the signal '.txt' file has an endline character.
    This funciton is used to strip that enline character.
    The next function after that allows conversion to float type data.
    """
    def stripSignal(self):
        for counter in range(0,len(self.signal)):                               # Iterate through all data in signal
            self.signal[counter] = fcnlib.stripNewline(self.signal[counter])    # Strip newline character
            
    def convertSignal(self):
        for counter in range(0,len(self.signal)):                   # Iterate through all values of signal
            self.signal[counter] = float(self.signal[counter])      # Convert values to float
   
    """ 
    This function uses a low-pass Hamming filter, applied to the ultrasonic signal.
    A ~100MHz bandpass (length 31) filter is used, sait seems to provide best results.
    A forward-backward smoothing algorithm is applied, via 'filtfilt'.
    """
    def smoothSignal(self):
        window = hamming(31)                                        # Create low-pass filter    
        denom = sum(window)                                         # Normalization of filter
        self.signal_smooth = filtfilt(window,denom,self.signal)     # Apply smoothing
        
    """
    Function used to get peaks from the smoothed signal.
    """
    def getPeaks(self):
        self.peaks = fcnlib.findPeaks(self.signal_smooth,self.THRESH,self.DEC)