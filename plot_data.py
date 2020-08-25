'''
Created on 31-Jul-2020

@author: mbarison
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd

from datetime import datetime, timedelta
import os
from Agencies import *

def plot_data(config):
        
    start_date = config["start_date"]
    tempdir    = config["tempdir"]
    verbose    = config.get("verbose", False)
    qstat_f    = config["qstats_f"]
    estat_f    = config["estats_f"]


    # Queue stats
    dfq = pd.read_csv(qstat_f)
    dfq["time"] = pd.Series([start_date+timedelta(seconds=i) for i in dfq["ticks"]])
    print("Overall queue stats:")
    print(dfq.describe())

    print("First hour:")
    print(dfq[dfq["hour"]==1].describe())
    
    print("Second hour:")
    print(dfq[dfq["hour"]==2].describe())
  
    print("Third hour:")
    print(dfq[dfq["hour"]>2].describe())

    ax = plt.gca()

    dfq[dfq["run"]==1].plot(x="time", y="length", ax=ax, legend=False)
    dfq[dfq["run"]==2].plot(x="time", y="length", ax=ax, legend=False)
    dfq[dfq["run"]==3].plot(x="time", y="length", ax=ax, legend=False)
    dfq[dfq["run"]==4].plot(x="time", y="length", ax=ax, legend=False)
    dfq[dfq["run"]==10].plot(x="time", y="length", ax=ax, legend=False)
    plt.savefig(os.path.join(tempdir, "queue_length.png"))

    # Employee stats
    dfe = pd.read_csv(estat_f)
    dfe = dfe[["run", "agency", "arrival", "place", "waiting_time", "hour"]]   
    dfe = dfe[dfe["agency"]==Agencies.EC.value]
    
    print("Single morning stats:")
    df_sm = dfe[dfe["run"]==4]
    print(df_sm .describe())
   
    print("First hour:")
    print(df_sm[df_sm["hour"]==1].describe())
    
    print("Second hour:")
    print(df_sm[df_sm["hour"]==2].describe())
  
    print("Third hour:")
    print(df_sm[df_sm["hour"]>2].describe()) 
    
    print("Overall Employee stats:")
    print(dfe.describe())
    
    print("First hour:")
    print(dfe[dfe["hour"]==1].describe())
    
    print("Second hour:")
    print(dfe[dfe["hour"]==2].describe())
  
    print("Third hour:")
    print(dfe[dfe["hour"]>2].describe())

    print("\n####################\nAveraged maximum")
    dfm = dfe[["run", "place", "waiting_time"]].groupby(by="run").max()
    print(dfm.describe())

    #dfq.plot(x="ticks", y="length")
    
    #plt.savefig("/tmp/queue_length.png")

    #for i in range(1,9):
    #    dfl.plot(x="ticks", y="lift_%d" % i)
    #    plt.savefig("/tmp/lift_%d.png" % i)

if __name__ == '__main__':
    plot_data()
    
    