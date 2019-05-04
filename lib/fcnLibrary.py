#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Mar 26, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: illustrative
"""

import  matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from scipy.signal import find_peaks   # Peak-finding alorithm

def stripNewline(str):                                  
    # Generic function to remove newline character from data entries
    newStr = str.rstrip('\n')
    return newStr                                       
    
def createTime(timeStep,axisLength):
    """
    # Function to create a time vector (used as x-data)
    # Uses the 'axisLength' parameter from the UT data file
    """
    timeVector = np.empty(int(axisLength),dtype=float)
    for counter in range(0,int(axisLength)):
        timeVector[counter] = timeStep*(counter)
    return timeVector

def createFrequencies(samplingRate,points):
    """
    # Function to create a frequency vector for the FT
    # Is made to handle even- and odd- number of points
    """
    arrayLength = int(np.floor(points/2))
    freqArray = np.empty(arrayLength)
    for counter in range(0,arrayLength):
        freqArray[counter] = counter*samplingRate/points
    return freqArray
    
def getTimeIndex(x_value,vector):
    """
    # Get the vector index for a given time. 
    # 'vector' must be montonic
    """
    reducedVector = vector-round(x_value,3)
    absVector = np.absolute(reducedVector)
    minValue = np.amin(absVector)
    idx = np.where(absVector==minValue)
    return int(idx[0])
    
def getTimeStep(start,end,axisLength): 
    """
    # Get time step, i.e. sample rate
    # Requires parameters from UT data file
    """
    timeDifference = float(end)-float(start)
    step = timeDifference/float(axisLength)
    return step
    
def findPeaks(signal,threshold,decrease_rate):
    """
    # Find peaks in ultrasonic signal
    # Use the Scipy 'find_peaks' function
    """
    peaks, _= find_peaks(signal)
    # Call 'findEchoes' function to apply thresholding parameters
    important_peaks = findEchoes(signal,peaks,threshold,decrease_rate)
    return important_peaks
    
def findEchoes(sig,pks,thresh,dec):
    """
    # Find the important peaks using thresholdin parameters.
    # 'sig' is the signal on which peaks are being found
    # 'pks' `holds the indices of peak locations
    # 'thresh' is the minimum for the first peak value
    # 'dec' is the rate of decrement for the next threholding
    """
    Idx = np.array([]) #Empty array
    for counter in range(len(pks)):
        if sig[pks[counter]]>(thresh*dec):
            Idx = np.append(Idx,pks[counter]) #Add peak to Idx array
    return Idx
    
def mapPeakTime(time_vect,idx):
    """
    # Find the time value of 'idx' values in 'time_vect'
    # Needs to be combined with function 'getTimeValue' or 'getTimeIndex'
    """
    pkTime = np.empty(len(idx),dtype=object) #Preallocate empty array
    for counter in range(0,len(idx)):
        pkTime[counter] = time_vect[int(idx[counter])]
    return pkTime
    
def mapPeaks(signal,idx):
    """
    # Use indices available to get peak voltages
    """
    pks = np.empty(len(idx),dtype=object)  # Preallocate array of empties
    for counter in range(0,len(idx)):
        pks[counter] = signal[int(idx[counter])]
    return pks

def calculateFT(signal,point):
    """
    # Calculate the 'point' numbered Fourier Transform
    # Uses numpy's 'fft' function from 'fft' module
    # 'P2' is the Two Sided Power Spectrum
    """
    transform = np.fft.fft(signal,point)
    P2 = np.absolute(transform)
    powerSpectrum = np.empty(int(np.floor(point/2)))
    powerSpectrum[0] = P2[0]
    for counter in range(1,int(np.floor(point/2))):
        powerSpectrum[counter] = P2[counter]*2
    return powerSpectrum
    
def calculateSamplingRate(signalObj):
    """
    # Calculate the sampling rate of an ultraosnic sgnal
    # Has to be from a 'signal' class object
    """
    duration = signalObj.duration
    axisLength = signalObj.axisLength
    return axisLength/duration
