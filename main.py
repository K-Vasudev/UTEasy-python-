#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Mar 26, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: illustrative
"""

# Import modules
from Vector import createVector
from Visual import createVisual
#from Signal import UltrasonicSignal
import FcnLibrary as fcnlib

def main():
    
    # Create main figure - call function with __init__ values
    #vis = UltrasonicSignal()
    
    #
    
    vis = createVisual()                                # Make figure and axes

    vect = createVector()                               # Make data vector   
    vect.readUltrasonic()                               # Read in ultrasonic data
    vect.convertSignal()                                # Convert signal from 'str' to 'float'
    vect.smoothSignal()                                             # Smooth ultrasonic signal
    timeVector = fcnlib.createTime(vect.step,vect.axisLength)       # Create xdata for plot (should convert to OOP)
    vis.addLine(timeVector,vect.signal_smooth)                      # Add vector data to plot
    vect.getPeaks()                                                 # Get the inidces of signal peaks
    pkTime = fcnlib.mapPeakTime(timeVector,vect.peaks)              # Create vector of peak times
    pkVolt = fcnlib.mapPeaks(vect.signal_smooth,vect.peaks)         # Create vector of signal peaks
    vis.addPeaks(pkTime,pkVolt)                                     # Add peaks to plot    
    vis.addButton()                                     # Add button to plot area
    vis.connectButton()                                 # Connect button to plot data
    vis.addLabels()                                     # Add axis labels
    
    vis.showplot()                                      # Make the figure appear                

if __name__ == '__main__':                              # Program entry point            
    main()