# Code used to read in ultrasonic file
# The file must be of the form created by ALxGTe1.0
#################################################

import  matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button,CheckButtons

class Index(object):
    def click(self, event):
        print('click')
        
    def check(self, event):
        print('check!')

def getParameters(data):                                # Get the basic signal parameters from a data signal
    AxisLength = stripNewline(data[1])
    Domain = stripNewline(data[3])
    return AxisLength, Domain

def stripNewline(str):                                  # Strip newline characters from 'str'
    newStr = str.rstrip('\n')
    return newStr

def getDomain(domain):                                  # Get the start and end times from 'Domain'
    Start,End,Units = domain.split()
    return Start,End

def stripSignal(signal):                                # Strip newlines from signal using 'stripNewline'
    for counter in range(0,len(signal)):
        signal[counter] = stripNewline(signal[counter])
    return signal
    
def convertSignal(signal):
    for counter in range(0,len(signal)):
        signal[counter] = float(signal[counter])
    return signal

def getTimeStep(axisLength,domain):                     # Use 'axisLength' and 'domain' for signal sampling period
    start,end = getDomain(domain)
    timeStep = (float(end)-float(start))/float(axisLength)
    return timeStep
    
def createTimeVector(timeStep,axisLength):
    timeVector = np.empty(int(axisLength),dtype=float)
    for counter in range(1,int(axisLength)):
        timeVector[counter-1] = timeStep*(counter-1)
    return timeVector
    
def createButton(axes_location,text,click_action):
    try:
        axbutton = plt.axes(axes_location)
    except:
        print('Error in createButton: Unable to create axes object. Check tuple size')
    button = Button(axbutton,text)
    button.on_clicked(click_action)
    return button
    
def createCheckButton(axes_location,text,click_action):
    try:
        axrbutton = plt.axes(axes_location)
    except:
        print('Error in createCheckButtion: Unable to create axes object. Check tuple size')
    state = [True]
    button = CheckButtons(axrbutton,text,state)
    button.on_clicked(click_action)
    return button

################################################
# Main body

Data = np.array([])                                     # 'data' contains secondary data for the signal

with open('TCPL_s3_c3_long_1.txt','r') as file:         # open UT signal file for reading
    for lines in range(0,7):                            # The first 7 lines are secondary data
        Data = np.append(Data,file.readline())
    AxisLength,Domain = getParameters(Data)             # Get parameters of 'AxisLength' and 'Domain'
    Signal = np.empty(int(AxisLength),dtype=object)
    counter = 0
    for f in file:                                      # The rest of the file is the ultrasonic signal
        Signal[counter] = f
        counter += 1
        
Signal = stripSignal(Signal)                            # Use 'StripLine' function to remove newline characters
Signal = convertSignal(Signal)                          # Use 'convertSignal' to change signal values to floats

StartTime,EndTime = getDomain(Domain)                   # Use 'getDomain' fcn to get the signal start and end times

TimeStep = getTimeStep(AxisLength,Domain)               

TimeVector = createTimeVector(TimeStep,AxisLength)

f, (ax1, ax2) = plt.subplots(2, 1)
plt.subplots_adjust(bottom=0.2)
ax1.plot(TimeVector,Signal)

callback = Index()
b1_axes = [0.1, 0.05, 0.1, 0.075]
b1 = createButton(b1_axes,'Button 1',callback.click)

b2_axes = [0.21, 0.05, 0.1, 0.075]
b2 = createCheckButton(b2_axes,['Button 2'],callback.check)


plt.show()