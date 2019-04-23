#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Mar 26, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: illustrative
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

class createVisual:

    def __init__(self):                             # Behavior on creation
        self.fig = plt.figure()                     # Create figure container
        self.ax = self.fig.add_subplot(1,1,1)       # Create axes object (plot)
        plt.subplots_adjust(bottom=0.2)             # Make room for button
        
    def showplot(self):
        plt.show()                                  # Make plot appear                
        
    def addButton(self):
        self.axButton = plt.axes([0.81, 0.05, 0.15, 0.075])      # Create axes object (button)
        #self.ax2Button = plt.axes([0.68, 0.05, 0.1, 0.075])      # Create axes object (button)
        self.toggleButton = Button(self.axButton,'Toggle Peaks')     # Set button parameters
        #self.flipButton = Button(self.ax2Button,'Flip Y')     # Set button parameters
        
    def connectButton(self):                                # Used to create button action
        #self.flipButton.on_clicked(self.flipYData)         # Call 'flipYData' on press
        self.toggleButton.on_clicked(self.togglePeaks)      # Call 'toggle_Button' on press
        
    def addLine(self,xdata,ydata):                  # Used to add signal line
        self.plotLine = self.ax.plot(xdata,ydata)   # Plot lines specified by x/y data
    
    def addPeaks(self,xdata,ydata):                         # Used to add signal peak markers
        self.peakLine = self.ax.plot(xdata,ydata,'ro')      # Plot line specified by x/y
        
    def togglePeaks(self,event):                            # Set action of button press    
        if self.peakLine[0].get_visible():                  # Check if peak markers are visible
            self.peakLine[0].set_visible(False)             # Turn peak markers off
        elif self.peakLine[0].get_visible()==False:         # Check if peak markers are off    
            self.peakLine[0].set_visible(True)              # Turn peak markers on
        plt.draw()                                          # Draw to the figure
        
    def flipYData(self,event):
        self.ydata = self.plotLine[0].get_ydata()   # Get plot ydata
        self.reverse_vector()                       # Call 'reverse_vector'
        self.plotLine[0].set_ydata(self.ydata)      # Set new ydata
        plt.draw()                                  # Update figure
        
    def reverse_vector(self):                       # Used to reverse vector
        self.ydata = np.flip(self.ydata)            # Simple numpy vector reverse
    
    def addLabels(self):
        self.ax.set_xlabel('Time (microsecond)')    # Set x-label
        self.ax.set_ylabel('Voltage (V)')           # Set y-label