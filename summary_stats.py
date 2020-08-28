'''
Created on 27-Aug-2020

@author: mbarison


Summary stats

'''

import numpy as np

def summary_stats(df):
    p  = np.percentile(df, [2.5, 97.5])
    mn = np.mean(df)
    mx = np.max(df)
    
    print("between %g and %g with 95%% CL, mean=%g, max=%g" % (p[0], p[1], mn, mx))
    
    df.plot.hist(bins=mx, density=True)
    
    return (p[0], p[1], mn, mx)