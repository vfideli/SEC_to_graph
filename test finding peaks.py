# -*- coding: utf-8 -*-
"""
Author:     Vincent Fideli
Created:     Thu Oct  7 10:58:08 2021

Description
-----------
Just messing around with a finding peaks code I found online.

"""

import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks

x = np.sin(2*np.pi*(2**np.linspace(2,10,1000))*np.arange(1000)/48000) + np.random.normal(0, 1, 1000) * 0.15
peaks, _ = find_peaks(x, distance=20)
peaks2, _ = find_peaks(x, prominence=1)      # BEST!
peaks3, _ = find_peaks(x, width=20)
peaks4, _ = find_peaks(x, threshold=0.4)     # Required vertical distance to its direct neighbouring samples, pretty useless
plt.subplot(2, 2, 1)
plt.plot(peaks, x[peaks], "xr"); plt.plot(x); plt.legend(['distance'])
plt.subplot(2, 2, 2)
plt.plot(peaks2, x[peaks2], "ob"); plt.plot(x); plt.legend(['prominence'])
plt.subplot(2, 2, 3)
plt.plot(peaks3, x[peaks3], "vg"); plt.plot(x); plt.legend(['width'])
plt.subplot(2, 2, 4)
plt.plot(peaks4, x[peaks4], "xk"); plt.plot(x); plt.legend(['threshold'])
plt.show()

#%% my test area
import numpy as np
import matplotlib.pyplot as plt 
from scipy.signal import find_peaks

x = np.linspace(0, 700, 70000)
y = np.sin(x)

peaks, _ = find_peaks(y, prominence=1)

# plt.plot(x,y)
plt.plot(x, y)
plt.plot(x[peaks], y[peaks], 'xr')

# plt.plot(peaks, y[peaks], 'x')