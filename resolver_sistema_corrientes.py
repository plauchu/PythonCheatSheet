#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 18:16:35 2021

@author: isaac
"""

import cmath
import numpy as np

def rad2grados(phi):
    return (phi*180)/np.pi
    
x = np.matrix([[1/250j,-1/250j+1/80+1/100,-1/100],
               [1,0,-1],
               [-1/250j,1/250j,-1/80j+1/80+1/100]]) 

y = np.array([0,150,0])
x_inv = np.linalg.inv(x)
resul = y @ x_inv
resul_polar = []
for i in range(3):
    mag, ang = cmath.polar(resul[0,i])
    ang = rad2grados(ang)
    resul_polar.append((mag,ang))
        

print(resul_polar)