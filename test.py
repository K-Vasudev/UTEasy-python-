#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Apr 26, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: full function

Unit Tests for some of the functions in the UTEasy library.
Uses the Arrange, Act, Assert setup.
"""

# Import modules
import lib.fcnLibrary as fcnlib
import numpy as np

"""
# Signal.py Tests
# Test the 'signal.py' UltrasonicSignal class
"""


"""
# fcnLibrary.py Tests
# Test the 'fcnLibrary' functions
"""

# Test for stripNewline
testStr01 = "String\n"
testStr02 = fcnlib.stripNewline(testStr01)
assert testStr02=="String","fcnlib.stripNewline Error"

# Test for createTime
testTime = fcnlib.createTime(1,5)
assert (testTime==[0,1,2,3,4]).all(),"fcnlib.createTime Error"

# Test for getTimeStep
start = 0
end = 10
axisLength = 10
timeStep = fcnlib.getTimeStep(start,end,axisLength)
assert timeStep==1,"Error in fcnlib.getTimeStep"

# Test mapPeakTime
time_vect = [0,1,2,3,4,5,6,7,8,9,10]
idx = [3,6,7]
peakTime = fcnlib.mapPeakTime(time_vect,idx)
assert (peakTime==idx).all(),"Error in fcnLibrary mapPeakTime()"
