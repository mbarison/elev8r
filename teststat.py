import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from Randomizer import Randomizer
from datetime import datetime, timedelta

import pandas as pd

date1 = datetime(2020, 9, 1, 6, 30)
date2 = datetime(2020, 9, 1, 9, 30)

dt = date2 - date1
print("Seconds:", dt.seconds)

r = Randomizer(dt.seconds, 1000)

arrival_times = []

for i in range(0, dt.seconds):
    if r.get_arrival():
        #arrival_times.append( date1 + timedelta(seconds=i) )
        arrival_times.append(i)
        
#print(arrival_times)

df = pd.DataFrame(arrival_times, columns=["Arrival Time (sec)"])

df.plot.kde()

plt.savefig("/tmp/arrival_kde.png")

df.plot.hist(bins=100)

plt.savefig("/tmp/arrival_hist.png")