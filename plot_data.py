'''
Created on 31-Jul-2020

@author: mbarison
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd

def plot_data():
    
    # Queue stats
    dfq = pd.read_csv("/tmp/queue_stats.csv")
    print("Overall queue stats:")
    print(dfq.describe())

    print("First hour:")
    print(dfq[dfq["hour"]==1].describe())
    
    print("Second hour:")
    print(dfq[dfq["hour"]==2].describe())
  
    print("Third hour:")
    print(dfq[dfq["hour"]>2].describe())

    # Employee stats
    dfe = pd.read_csv("/tmp/employee_stats.csv")
    dfe = dfe[["arrival", "place", "waiting_time", "hour"]]   
    print("Overall Employee stats:")
    print(dfe.describe())
    
    print("First hour:")
    print(dfe[dfe["hour"]==1].describe())
    
    print("Second hour:")
    print(dfe[dfe["hour"]==2].describe())
  
    print("Third hour:")
    print(dfe[dfe["hour"]>2].describe())

    #dfq.plot(x="ticks", y="length")
    
    #plt.savefig("/tmp/queue_length.png")

    #for i in range(1,9):
    #    dfl.plot(x="ticks", y="lift_%d" % i)
    #    plt.savefig("/tmp/lift_%d.png" % i)

if __name__ == '__main__':
    plot_data()
    
    