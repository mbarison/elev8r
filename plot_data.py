'''
Created on 31-Jul-2020

@author: mbarison
'''

import matplotlib
matplotlib.use('cairo', warn=False, force=True)
import matplotlib.pyplot as plt

import pandas as pd

from datetime import datetime, timedelta
import os
from Agencies import *

from erlang_fit import *
from summary_stats import *
from lifts_stackplot import *

def plot_queue(config):
    
    start_date = config["start_date"]
    tempdir    = config["tempdir"]
    verbose    = config.get("verbose", False)
    qstat_f    = config["qstats_f"]

    
    dfq = pd.read_csv(qstat_f)
    dfq["time"] = pd.Series([start_date+timedelta(seconds=i) for i in dfq["ticks"]])
    print("\n\n#################################\nOverall queue stats:")
    #print(dfq.describe())
    plt.figure(figsize=[12,10])
    plt.suptitle('Queue Length')

    ax = plt.subplot(411)
    summary_stats(dfq["length"])
    plt.gca().set_title('Overall')
    plt.gca().set_yscale('log') 

    
    print("First hour:")
    #print(dfq[dfq["hour"]==1].describe())
    plt.subplot(412, sharex=ax)
    summary_stats(dfq[dfq["hour"]==1]["length"])
    plt.gca().set_title('First hour')
    plt.gca().set_yscale('log') 

    print("Second hour:")
    #print(dfq[dfq["hour"]==2].describe())
    plt.subplot(413, sharex=ax)
    summary_stats(dfq[dfq["hour"]==2]["length"])
    plt.gca().set_title('Second hour')
    plt.gca().set_yscale('log') 
  
    print("Third hour:")
    #print(dfq[dfq["hour"]>2].describe())
    plt.subplot(414, sharex=ax)
    summary_stats(dfq[dfq["hour"]>2]["length"])
    plt.gca().set_title('Third hour')
    plt.gca().set_yscale('log') 
    
    plt.show()
    plt.savefig(os.path.join(tempdir, "queue_stats.png"))
    plt.close()
    
    del dfq
    

def plot_erlang(config):
    
    start_date = config["start_date"]
    tempdir    = config["tempdir"]
    verbose    = config.get("verbose", False)
    estat_f    = config["estats_f"]
    
    dfe = pd.read_csv(estat_f)
    dfe = dfe[["run", "agency", "arrival", "place", "waiting_time", "hour"]]   

    print('\n\n#################################\nErlang fits')
    plt.figure(figsize=[12,10])
    plt.suptitle("Erlang distribution arrival times")

    ax = plt.subplot(311)
    erlang_fit(dfe[dfe["hour"]==1][["run", "arrival"]], 50)
    plt.gca().set_yscale('log') 

    plt.subplot(312, sharex=ax)
    erlang_fit(dfe[dfe["hour"]==2][["run", "arrival"]], 50)
    plt.gca().set_yscale('log') 

    plt.subplot(313, sharex=ax)
    erlang_fit(dfe[dfe["hour"]>2][["run", "arrival"]], 50)
    plt.gca().set_yscale('log') 
    plt.gca().set_xlabel("seconds")

    plt.show()
    plt.savefig(os.path.join(tempdir, "erlang_fits.png"))
    plt.close()

    del dfe


def plot_employees(config):
    
    start_date = config["start_date"]
    tempdir    = config["tempdir"]
    verbose    = config.get("verbose", False)
    estat_f    = config["estats_f"]

    dfe = pd.read_csv(estat_f)
    dfe = dfe[["run", "agency", "arrival", "place", "waiting_time", "hour"]]   
    
    dfe = dfe[dfe["agency"]==Agencies.EC.value]

    print('\n\n#################################\nEmployee waiting times:')
    plt.figure(figsize=[12,10])
    plt.suptitle("Employee waiting times")

    ax = plt.subplot(411)
    #print(dfe.describe())
    summary_stats(dfe["waiting_time"])
    plt.gca().set_title('Overall')
    plt.gca().set_yscale('log') 
    
    ax = plt.subplot(412, sharex=ax)
    print("First hour:")
    #print(dfe[dfe["hour"]==1].describe())
    summary_stats(dfe[dfe["hour"]==1]["waiting_time"])
    plt.gca().set_title('First hour')
    plt.gca().set_yscale('log') 
    
    ax = plt.subplot(413, sharex=ax)
    print("Second hour:")
    #print(dfe[dfe["hour"]==2].describe())
    summary_stats(dfe[dfe["hour"]==2]["waiting_time"])
    plt.gca().set_title('Second hour')
    plt.gca().set_yscale('log') 
  
    ax = plt.subplot(414, sharex=ax)
    print("Third hour:")
    #print(dfe[dfe["hour"]>2].describe())
    summary_stats(dfe[dfe["hour"]>2]["waiting_time"])
    plt.gca().set_title('Third hour')
    plt.gca().set_yscale('log') 
    
    plt.show()
    plt.savefig(os.path.join(tempdir, "employee_stats.png"))
    plt.close()
    
    del dfe


def plot_lifts(config):
    
    start_date = config["start_date"]
    tempdir    = config["tempdir"]
    verbose    = config.get("verbose", False)
    lstat_f    = config["lstats_f"]
    
    dfl = pd.read_csv(lstat_f)
    dfl["time"] = pd.Series([start_date+timedelta(seconds=i) for i in dfl["ticks"]])
    print("\n\n#################################\nLift stats:")

    plt.figure(figsize=[12,10])
    plt.suptitle('Lift status')

    plt.subplot(411)
    lifts_stackplot(dfl)
    plt.gca().set_title('Overall')

    plt.subplot(412)
    lifts_stackplot(dfl[dfl["hour"]==1])
    plt.gca().set_title('First hour')

    plt.subplot(413)
    lifts_stackplot(dfl[dfl["hour"]==2])
    plt.gca().set_title('Second hour') 
  
    plt.subplot(414)
    lifts_stackplot(dfl[dfl["hour"]>2])
    plt.gca().set_title('Third hour')
    
    plt.show()
    plt.savefig(os.path.join(tempdir, "lift_stats.png"))
    plt.close()
    
    del dfl
    

def plot_data(config, p_queue=True, p_erlang=True, p_employees=True, p_lifts=True):
        
    start_date = config["start_date"]
    tempdir    = config["tempdir"]
    verbose    = config.get("verbose", False)
    qstat_f    = config["qstats_f"]
    estat_f    = config["estats_f"]
    lstat_f    = config["lstats_f"]


    # Queue stats
    if p_queue:
        plot_queue(config)


    #ax = plt.gca()

    #dfq[dfq["run"]==1].plot(x="time", y="length", ax=ax, legend=False)
    #dfq[dfq["run"]==2].plot(x="time", y="length", ax=ax, legend=False)
    #dfq[dfq["run"]==3].plot(x="time", y="length", ax=ax, legend=False)
    #dfq[dfq["run"]==4].plot(x="time", y="length", ax=ax, legend=False)
    #dfq[dfq["run"]==10].plot(x="time", y="length", ax=ax, legend=False)
    #plt.savefig(os.path.join(tempdir, "queue_length.png"))

    # Employee stats
    if p_erlang:
        plot_erlang(config)
        
#    print("Single morning stats:")
#    df_sm = dfe[dfe["run"]==4]
#    print(df_sm .describe())
#   
#    print("First hour:")
#    print(df_sm[df_sm["hour"]==1].describe())
#    
#    print("Second hour:")
#    print(df_sm[df_sm["hour"]==2].describe())
#  
#    print("Third hour:")
#    print(df_sm[df_sm["hour"]>2].describe()) 
    
    if p_employees:
        plot_employees(config)


    #print("\n####################\nAveraged maximum")
    #dfm = dfe[["run", "place", "waiting_time"]].groupby(by="run").max()
    #print(dfm.describe())

    #dfq.plot(x="ticks", y="length")
    
    #plt.savefig("/tmp/queue_length.png")

    #for i in range(1,9):
    #    dfl.plot(x="ticks", y="lift_%d" % i)
    #    plt.savefig("/tmp/lift_%d.png" % i)

    
    # Lift stats
    if p_lifts:
        plot_lifts(config)


if __name__ == '__main__':
    plot_data()
    
    