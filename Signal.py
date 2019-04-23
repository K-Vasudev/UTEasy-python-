#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday, Apr 22, 2019
@author: kvasudev
@email: kvasudev@ualberta.ca
@status: illustrative
"""

# Import modules
import numpy as np

class UltrasonicSignal:

    UT_FILE = 'UltrasonicSignal.txt'

    def __init__(self):
        try:
            f = open(self.UT_FILE,'r')
            f.close()
        except:
            print('ERROR: COULD NOT OPEN FILE - SEE Vector.py')