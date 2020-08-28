'''
Created on 27-Aug-2020

@author: mbarison


Fit Erlang distribution (k=1, exponential) to time arrival data

'''

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def erlang_fit(df, nbins=50):

    tmp=[]
    
    print("Data points=%d" % len(df))
    
    for i in range(1, len(df)):
        if df["run"].iloc[i] == df["run"].iloc[i-1]:
            dt = df["arrival"].iloc[i]-df["arrival"].iloc[i-1]
            if dt >= 0:                        
                tmp.append(dt)

    dfp = pd.Series(tmp)

    #print("Diff points=%d" % len(dfp))

    bin_heights, bin_borders, _ = plt.hist(dfp, bins=nbins, density=True)
    
    bin_centers = bin_borders[:-1] + np.diff(bin_borders) / 2
    
    def erlang(x, lamb, scale):
        return scale * np.exp(-lamb*x)
    
    popt, pcov = curve_fit(erlang, bin_centers, bin_heights, p0=[1., bin_heights[0]])
    perr = np.sqrt(np.diag(pcov))
    
    
    residuals = bin_heights - erlang(bin_centers, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((bin_heights-np.mean(bin_heights))**2)

    r_squared = 1 - (ss_res / ss_tot)

    
    print("Fit results: lambda=%g scale=%g" % (popt[0], popt[1]))
    print("Fit error: eps_lambda=%g eps_scale=%g" % (perr[0], perr[1]))
    print("R-squared=%g" % r_squared)
    
    x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)

    plt.plot(x_interval_for_fit, erlang(x_interval_for_fit, *popt), label='fit', c='red')

    xpos = plt.gca().get_xlim()[1]/3
    ypos = bin_heights[0]*.8

    plt.text(xpos, ypos, "lambda=%.3g\u00b1%.3g R-squared=%.3g" % (popt[0], perr[0], r_squared))
    