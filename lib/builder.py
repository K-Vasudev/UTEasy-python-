#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Apr 22, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: full function with limitations
"""

# Import modules
from lib.handler import SignalHandler,PeakHandler,FTHandler
from lib.button_handler import ButtonObject
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def Builder():
    # Create figure
    fig = plt.figure("UTEasy",figsize=(8,6))

    """
    Create axis object holding signal
    Create axis object holding FT
    """
    axSignal = fig.add_axes([0.1,0.6,0.7,0.3])
    axFT = fig.add_axes([0.1,0.1,0.7,0.3])
    """ End of plot axes creation """

    
    """
    Create handler objects
    1)Signal Handler - Reads ultrasonic signal and manipulates it
    2)Peak Handler - Takes ultrasonic data to and calculates peak locations
    3)FT Handler - Calculates Fourier transform and handlers plotting
    """
    signalHandler = SignalHandler(axSignal)
    peakHandler = PeakHandler(axSignal,signalHandler)
    ftHandler = FTHandler(axFT,signalHandler)
    """ End of creation of handlers """
    
    
    """
    Create callback instance of ButtonObject
    This is used to attach all buttons
    """
    callback = ButtonObject(
        signalHandler,peakHandler,ftHandler)
    """ Callback created """
    
    
    """
    Create button axes objects
    1) Toggle smoothing buttons
    2) Toggle peak markers
    3) Toggle padding
    4) Calculate Fourier Transform    
    """
    smoothBtnAx = fig.add_axes([0.81, 0.8, 0.18, 0.075])
    smoothButton = Button(smoothBtnAx,'Smoothing: On')
    smoothButton.on_clicked(callback.toggleSmoothing)
    callback.setSmoothButton(smoothButton)
    
    peaksBtnAx = fig.add_axes([0.81, 0.65, 0.18, 0.075])
    peaksButton = Button(peaksBtnAx,'Peaks: On')
    peaksButton.on_clicked(callback.togglePeaks)
    callback.setPeakButton(peaksButton)
    
    paddingBtnAx = fig.add_axes([0.81, 0.345, 0.18, 0.075])
    paddingButton = Button(paddingBtnAx,'Zero-Padding: On')
    paddingButton.on_clicked(callback.togglePadding)
    callback.setPaddingButton(paddingButton)
    
    filterBtnAx = fig.add_axes([0.81, 0.22, 0.18, 0.075])
    filterButton = Button(filterBtnAx, 'FT Filtering: On')
    filterButton.on_clicked(callback.toggleFilter)
    callback.setFilterButton(filterButton)
    
    calcFTAx = fig.add_axes([0.81, 0.095, 0.18, 0.075])
    calcFTButton = Button(calcFTAx,'Calculate FT')
    calcFTButton.on_clicked(callback.calculateFT)
    """ 
    Buttons created and connected 
    """
    
    
    # Create and show the plot
    plt.show()
