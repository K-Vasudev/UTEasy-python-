#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Mar 26, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: full function with limitations
"""

# Import modules
import numpy as np
import matplotlib.pyplot as plt

"""
This class holds all the actions taken by button objects
"""
class ButtonObject:

    def __init__(self,sigHandle,pkHandle,ftHandle):
        """ 
        # Initialize the buttons to the various handlers
        # Handlers are from 'handler' file
        """
        self.signalTarget = sigHandle
        self.peakTarget = pkHandle
        self.ftTarget = ftHandle

    def togglePeaks(self,event):
        """
        # Toggle between peak visibility
        """
        self.peakTarget.setLineVisibility()
        self.changePeaksText()
        plt.draw()
        
    def changePeaksText(self):
        """ Alternate 'On' and 'Off' on button text """
        if self.peakTarget.getLineVisibility():
            self.peakButton.label.set_text("Peaks: On")
        else:
            self.peakButton.label.set_text("Peaks: Off")
        
    def toggleSmoothing(self,event):
        """
        # Set ultrasonic signal Y-Data.
        # Choose from smooth or un-smoothed signal
        """
        self.signalTarget.toggleSmoothing()
        self.changeSmoothText()
        plt.draw()
        
    def changeSmoothText(self):
        """ Alternate 'On' and 'Off' on button text """
        if self.signalTarget.smoothBool:
            self.smoothButton.label.set_text("Smoothing: On")
        else:
            self.smoothButton.label.set_text("Smoothing: Off")
        
    def togglePadding(self,event):
        """
        # Toggle zero-padding on the FT
        """
        self.ftTarget.togglePadding()
        self.changePaddingText()
        plt.draw()
        
    def changePaddingText(self):
        """ Alternate 'On' and 'Off' on button text """
        if self.ftTarget.padBool:
            self.paddingButton.label.set_text("Zero-Padding: On")
        else:
            self.paddingButton.label.set_text("Zero-Padding: Off")
        
    def toggleFilter(self,event):
        """
        # Toggle filtering of the signal
        # prior to Fourier Transform calculation
        """
        self.ftTarget.toggleFilter()   
        self.changeFilterText()
        plt.draw()
        
    def changeFilterText(self):
        """ Alternate 'On' and 'Off' on button text """
        if self.ftTarget.filtBool:
            self.filterButton.label.set_text("FT Filtering: On")
        else:
            self.filterButton.label.set_text("FT Filtering: Off")
        
    def calculateFT(self,event):
        """
        # Calculate and plot the Fourier Trasnform
        """
        self.ftTarget.applyTransform()
        plt.draw()
        
    def setPeakButton(self,button):
        """
        # Gives the button callback access to the button
        # Used to change button text, for example
        """
        self.peakButton = button
    def setSmoothButton(self,button):
        self.smoothButton = button
    def setFilterButton(self,button):
        self.filterButton = button   
    def setPaddingButton(self,button):
        self.paddingButton = button
