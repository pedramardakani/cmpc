# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:41:20 2019

@author: Pedram
"""
import sys
import numpy as np

p = int(sys.argv[1]);
q = int(sys.argv[2]);
angle = 90 * (1 - 2 * (q/p));
proceed = True;
pf = 1;
passes = 0;
points = np.array(1);
while proceed:
    pf += q;
    passes += 1;
    if pf > p:
        pf -= p;
    if pf == 1:
        proceed = False;
        #passes -= 1;
    if passes > p:
        print('The loop has a bug! Crashing ...');
        break;
        #print('pass = ',passes)
    #print('we\'re here: p = ',pf);
    points = np.append(points,pf)
         
lastMirr = points[-2];

print('incidence angle =',angle)
print('number of passes =',passes);
# print('last mirror number:',lastMirr) # for ZEMAX
# print('last mirror angle:', 360 - (180 - 2 * angle)) # for ZEMAX
