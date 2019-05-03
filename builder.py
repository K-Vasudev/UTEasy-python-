#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Apr 22, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: illustrative
"""

# Import modules
from handler import SignalHandler,PeakHandler,FTHandler
from button_handler import ButtonObject
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def Builder():
    # Create figure
    fig = plt.figure("UTEasy")

    """
    Create axis object holding signal
    Create axis object holding FT
    """
    axSignal = fig.add_axes([0.1,0.5,0.7,0.4])
    axFT = fig.add_axes([0.1,0.05,0.7,0.4])

    """
    Create handler objects
    1)Signal Handler
    2)Peak Handler
    3)FT Handler
    """
    signalHandler = SignalHandler(axSignal)
    signalHandler.plotLines()
    peakHandler = PeakHandler(axFT)
    ftHandler = FTHandler()
    
    """
    Create callback instance of ButtonObject
    This is used to attach all buttons
    """
    callback = ButtonObject(signalHandler)
    
    """
    Create button axes objects
    """
    filterBtn = fig.add_axes([0.81, 0.75, 0.15, 0.075])
    filterButton = Button(filterBtn,'Filter')
    filterButton.on_clicked(callback.toggleSmoothing)
    
    peaksBtn = fig.add_axes([0.81, 0.6, 0.15, 0.075])
    peaksButton = Button(peaksBtn,'Peaks')
    peaksButton.on_clicked(callback.togglePeaks)
    
    plt.show()
