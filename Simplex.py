#!/usr/bin/env python

import sys, math
import os, shutil, signal
#import commands
import subprocess as commands
import re
import random
import numpy as np
import matplotlib.pyplot as plt
import time
import multiprocessing
import itertools
import timeit

from scipy import optimize
from cosy import cosyrun 

# Hyper-parameters
numSteps = int(sys.argv[1]) # Number of steps

# Nominal quad fields at pole tip
qNom = [-0.39773, 0.217880+0.001472, 0.242643-0.0005+0.000729, -0.24501-0.002549, 0.1112810+0.00111, 0.181721-0.000093+0.00010-0.000096, -0.0301435+0.0001215] 

initial = np.asarray([random.uniform(qNom[i]*0.8, qNom[i]*1.2) for i in range(7)]) 
print(initial)

#Removing files from older runs
cmd = 'rm -f results.txt'		
failure, output = commands.getstatusoutput(cmd)


minimum = optimize.fmin(cosyrun, initial, maxiter = numSteps, full_output = 1, retall = 1)

 


