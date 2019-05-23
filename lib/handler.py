#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Mar 26, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: full function with limitations
"""

# Import modules
import lib.fcnLibrary as fcnlib
from lib.signal import UltrasonicSignal
import matplotlib.pyplot as plt
import numpy as np


class SignalHandler:

    def __init__(self,ax):
        """
        # Initialize the signal handler
        # Creates and wraps a UltrasonicSignal object ('signalObj')
        # Attaches to signal axis object ('axis')
        # Automatically plots signal and peak lines
        """
        self.smoothBool = True
        self.axis = ax
        self.populateSignalHandler()
        
    def populateSignalHandler(self):
        """
        # This function adds the ultrasonic signal object from signal.py
        # Additionally, determines the time vector, smooth signal,
        # and sets plot values related to the ultrasonic signal
        """
        self.signalObj = UltrasonicSignal()
        self.signalObj.acquireSignal()
        self.signal = self.signalObj.signal
        self.smoothSignal = self.signalObj.signalSmooth
        self.timeVector = self.signalObj.timeVector
        self.setSignalPlotTitle()
        self.setSignalAxisTitles()
        self.plotLines()
        
    def setSignalPlotTitle(self):
        """ Set plot title """
        self.axis.set_title("Ultrasonic Signal")
        
    def setSignalAxisTitles(self):
        """ Set axis titles """
        self.axis.set_xlabel("Time (microseconds)")
        self.axis.set_ylabel("Signal Voltage (V)")
       
    def findSignalPeaks(self):
        """ Finds signal peaks to pass to the peak handler"""
        self.signalPeaks = fcnlib.findPeaks(
            self.signalObj.signal,self.THRESH,self.DEC)
        
    def plotLines(self):
        """ 
        # Plot the ultrasonic signal 
        # Only used on first plot, setSignalYData used after that
        """
        self.signalLine = self.axis.plot(self.timeVector,self.smoothSignal)
        self.signalLine[0].set_linewidth(0.5)
        
    def toggleSmoothing(self):
        """ 
        # Toggle smoothing of the ultrasonic signal 
        # This is accessed by the smoothing button
        """
        self.smoothBool = not self.smoothBool
        self.setSignalYData()
            
    def setSignalYData(self):
        """
        # Set the Y Data of the signal plot
        # This is called indirectly by the button
        """
        if self.smoothBool:
            self.signalLine[0].set_ydata(self.smoothSignal)
        else:
            self.signalLine[0].set_ydata(self.signal)
    
    def setAxis(self,ax):
        """ Set the handler's axis object """
        self.axis = ax
        
    def getAxis(self):
        """ Get the handler's axis object """
        return self.axis
        
    def getPlotXLim(self):
        """ Get the axis' X Limits """
        return self.axis.get_xlim()
        
    def getPlotYLim(self):
        """ Get the axis' Y Limits """
        pass
        
    def getTimeIndices(self):
        """ Get the indices of the limits of the x axis """
        [timeMin,timeMax] = self.getPlotXLim()
        timeMinIdx = fcnlib.getTimeIndex(timeMin,self.timeVector)
        timeMaxIdx = fcnlib.getTimeIndex(timeMax,self.timeVector)
        return timeMinIdx,timeMaxIdx

class PeakHandler:
    # Class variables definition
    # Default THRESH = 0.5 and DEC = 0.2
    THRESH = 0.5
    DEC = 0.2

    def __init__(self,pkAxes,signalHandler):
        """
        # Initializer for the peak handler
        # It needs access to the signalHandler for getting peaks
        # This plot runs automatically and starts with peaks shown
        """
        self.axis = pkAxes
        self.signalHandler = signalHandler
        self.findSignalPeaks()
        self.plotLines()
        
    def findSignalPeaks(self):
        """
        # Find the Signal peaks indices
        # THen finds the corresponding voltages
        # Also finds the signal peak times
        """
        self.peakIndices = fcnlib.findPeaks(
            self.signalHandler.smoothSignal,self.THRESH,self.DEC)
        self.peakVoltages = fcnlib.mapPeaks(
            self.signalHandler.smoothSignal,self.peakIndices)
        self.peakTimes = fcnlib.mapPeakTime(
            self.signalHandler.timeVector,self.peakIndices)

    def plotLines(self):
        """ Plot the peaks """
        self.peakLine = self.axis.plot(self.peakTimes,self.peakVoltages,'ko')
        self.peakLine[0].set_markersize(3)
        
    def setLineVisibility(self):
        """ 
        # Toggle visibility
        # This is called by the PeakButton object in button_handler
        """
        self.peakLine[0].set_visible(
            not self.peakLine[0].get_visible())
            
    def getLineVisibility(self):
        """
        # Returns the visibility of the line with signal peaks.
        """
        return self.peakLine[0].get_visible()
        
class FTHandler:
    # Set class variables
    # Default: FT_POINT = 65536
    FT_POINT = 65536

    def __init__(self,ftAxes,signalHandler):
        self.signalHandler = signalHandler
        self.axis = ftAxes
        self.setFTPlotTitle()
        self.setFTAxisTitles()
        self.filtBool = True
        self.padBool = True
        
    def setFTPlotTitle(self):
        """ Set axis title """
        self.axis.set_title("Fourier Transform Power Spectrum")
        
    def setFTAxisTitles(self):
        """ Set axis titles """
        self.axis.set_xlabel("Frequency (MHz)")
        self.axis.set_ylabel("Voltage (mV)")        
    
    def applyTransform(self):
        """ 
        First use acquireTimeSignal for original
        """
        self.acquireTimeSignal()
        self.filterSignal()
        self.createFreqDomain()
        self.calculateFT()
        self.plotFTLine()
        
    def acquireTimeSignal(self):
        """ Get the time signal from the signalHandler """
        [timeMinIdx,timeMaxIdx] = self.signalHandler.getTimeIndices()
        if self.signalHandler.smoothBool:
            self.signalPart = self.signalHandler.smoothSignal[
                timeMinIdx:timeMaxIdx]
        else:
            self.signalPart = self.signalHandler.signal[
                timeMinIdx:timeMaxIdx]
        
    def filterSignal(self):
        """ 
        # Filter the signal, if filtBool is True 
        # Filtering is accomplished by multiplying
        # the signal portion by a hamming window of
        # equal size.
        """
        if self.filtBool:
            signalPartSize = self.signalPart.size
            hammingWindow = np.hamming(signalPartSize)
            self.signalPart = np.multiply(hammingWindow,self.signalPart)
        
    def createFreqDomain(self):
        """
        # Create the frequency domain used for plotting
        # Depends on zero-padding
        # If there is zero-padding, the freq. domain must
        # be the size of the zero-padded signal, otherwise
        # it is only as big as the signal portion
        """
        samplingRate = fcnlib.calculateSamplingRate(
            self.signalHandler.signalObj)
        if self.padBool:
            # If signal is padded, create a large freq domain
            self.freqDomain = fcnlib.createFrequencies(
                samplingRate,self.FT_POINT)
        else:
            # If signal isn't padded, create small freq domain
            self.freqDomain = fcnlib.createFrequencies(
                samplingRate,self.signalPart.size)
    
    def calculateFT(self):
        """
        # Calculate the N-point fourier transform.
        # Where N-point is either the size of FT_POINT
        # or the length of the signal portion from signal handler.
        # Specificially calculate the power spectrum.
        # Calculation is accomplished in functionLibrary.
        """
        if self.padBool:
            # If zero-padding is used
            self.powerSpectrum = fcnlib.calculateFT(
                self.signalPart,self.FT_POINT)
        else:
            # If zero padding isn't used
            ftPoint = int(self.signalPart.size)
            self.powerSpectrum = fcnlib.calculateFT(
                self.signalPart,ftPoint)
            
    def plotFTLine(self):
        """ Plot the Fourier Transform """
        self.ftLine = self.axis.plot(self.freqDomain,self.powerSpectrum)
        self.ftLine[0].set_linewidth(0.5)
        
    def setFilterBool(self,value):
        """ Set the filtering boolean value """
        self.filtBool = value
        
    def getFilterBool(self):
        """ Get the filtering boolean value """
        return self.filtBool
        
    def toggleFilter(self):
        """ Toggle whether filtering is applied """
        self.setFilterBool(not self.getFilterBool())
        
    def setPadBool(self,value):
        """ Set whether padding is used (boolean) """
        self.padBool = value
        
    def getPadBool(self):
        """ Get the boolean value of padding """
        return self.padBool
        
    def togglePadding(self):
        """ Toggle whether padding is applied """
        self.setPadBool(not self.getPadBool())
    
"""
In this module:
(Still requires some additions)

Classes:
    SignalHandler
        Methods:
            -add-
        Properties:
            signalObj
            signal
            smoothSignal
            timeVector
            axis
            signalLine
    PeakHandler
        Methods:
            -add-
        Properties:
            THRESH (class var)
            DEC (class var)
            axis
            signalHandler
            peakIndices
            peakVoltages
            peakTimes
            peakLine
    FTHandler
        Methods:
            -add-
        Properties:
            FILTER_SIZE (class var)
            FT_POINT (class var)
            axis
            signalHandler
            signalPart
            transform
            powerSpectrum
            
""" 
