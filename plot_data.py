'''
Created on 31-Jul-2020

@author: mbarison
'''

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd

from datetime import datetime, timedelta

def plot_data():
    
    sd = datetime(2020, 9, 1, 6, 30)
    
    # Queue stats
    dfq = pd.read_csv("/tmp/queue_stats.csv")
    dfq["time"] = pd.Series([sd+timedelta(seconds=i) for i in dfq["ticks"]])
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
    plt.savefig("/tmp/queue_length.png")

    # Employee stats
    dfe = pd.read_csv("/tmp/employee_stats.csv")
    dfe = dfe[["run", "arrival", "place", "waiting_time", "hour"]]   
    
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
    
    