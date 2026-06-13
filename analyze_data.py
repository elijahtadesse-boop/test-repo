from cProfile import label

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('.venv/daten/SDS00001.CSV', sep=",", skiprows=2)


# Set custom column names for the DataFrame.
# These names are used to access the respective columns easily (e.g., 'x', 'y', 'xerr', 'yerr').
# Adjust the column names according to the actual data structure of your file.
data.columns = ['time', 'CH1', 'CH2',]
time=data["time"]
ch1=data["CH1"]
ch2=data["CH2"]
#ch1 = float(np.array(ch1))
#ch2 = np.array(ch2))

difference = ch1 - ch2
fig, ax = plt.subplots(figsize=(8, 6))
#ax.set_ylim(0,2)
#print(adcSorted)
ax.scatter(time*1000, ch1, label="CH1", s=10)
ax.scatter(time*1000, ch2, label="CH2", s=10)
ax.scatter(time*1000, difference, label="Spannung", s=10)
#ax.set_ylim(0,3)
ax.set_xlabel("Zeit t/ms")
ax.set_ylabel("Spannung U/V")
#ax.hist(data["adc"], bins=100, color="royalblue", edgecolor="black", log=True)
# Filtert alle Werte unter 100 einfach heraus
# Neues Histogramm nur mit den hohen Signalen plottem
ax.legend()
plt.show()

