'''
Created on 28-Aug-2020

@author: mbarison
'''

import matplotlib.pyplot as plt

def lifts_stackplot(df):

    plt.stackplot(df["time"], df["ready"], df["idle"], df["in_transit"], df["homebound"], 
                    baseline='zero',
                    labels=["ready", "idle", "in_transit", "homebound"], 
                    colors=["green", "grey", "yellow", "blue"])