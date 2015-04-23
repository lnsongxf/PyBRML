#!/usr/bin/env python

"""
MATLAB's ismember() equivalent 
"""
import numpy as np

def ismember(x, y):
	x0 = x
	x = np.array(x)
	y = np.array(y)

	if x.ndim != y.ndim:
                print("Array dimension mismatch")
		x = np.array([x0])

	m = np.in1d(x,y)
	u = np.unique(x[m])
	index = np.array([(np.where(y == i))[0][-1] if t else 0 for i,t in zip(a,m)])
	return m, index
