#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import  matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from scipy.signal import find_peaks                     # Peak-finding alorithm

def stripNewline(str):                                  # Generic function to remove newline
    newStr = str.rstrip('\n')                           # Remove newline character from string
    return newStr                                       
    
def createTime(timeStep,axisLength):                        # Create a time vector (used as x-data)
    timeVector = np.empty(int(axisLength),dtype=float)      # Create empty vector of length 'axisLength'
    for counter in range(0,int(axisLength)-1):              # Iterate through vector length
        timeVector[counter] = timeStep*(counter)            # Set time-vector values
    return timeVector
    
def getTimeIndex(x_value,vector):                                   # Find the index location of 'x_value' in the monotonic vector 'vector'
    idx = np.where(np.around(vector,decimals=3)==round(x_value,3))  # Find where in 'vector' appears 'x_value'
    return idx[0]
    
def getTimeStep(start,end,axisLength):                  # Determine time-step from signal values    
    timeDifference = float(end)-float(start)            # Find the total signal length (in time)
    step = timeDifference/float(axisLength)             # Determine the sampling period
    return step
    
def findPeaks(signal,threshold,decrease_rate):                  # Function used to find ultrasonic signal peaks
    peaks, _= find_peaks(signal)                                        # Use Scipy 'find_peaks'
    important_peaks = findEchoes(signal,peaks,threshold,decrease_rate)  # Call 'findEchoes' function
    return important_peaks
    
def findEchoes(sig,pks,thresh,dec):
    Idx = np.array([])                          # Create empty numpy array
    for counter in range(len(pks)):             # Iterate over all peaks
        if sig[pks[counter]]>(thresh*dec):      # Conditional check
            Idx = np.append(Idx,pks[counter])   # Add passing peaks to 'Idx'
    return Idx
    
def mapPeakTime(time_vect,idx):                             # Use indices to get time of signal peaks
    pkTime = np.empty(len(idx),dtype=object)                # Preallocate array of empties
    for counter in range(0,len(idx)):                       # Use all 'idx' values
        pkTime[counter] = time_vect[int(idx[counter])]      # Get time of signal peaks
    return pkTime
    
def mapPeaks(signal,idx):                                   # Use indices to get signal peak voltages
    pks = np.empty(len(idx),dtype=object)                   # Preallocate array of empties
    for counter in range(0,len(idx)):                       # Use all 'idx' values
        pks[counter] = signal[int(idx[counter])]            # Get voltage of signal peaks
    return pks