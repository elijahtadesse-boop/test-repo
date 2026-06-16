
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('daten/SDS00013.CSV', sep=",", skiprows=2)


# Set custom column names for the DataFrame.
# These names are used to access the respective columns easily (e.g., 'x', 'y', 'xerr', 'yerr').
# Adjust the column names according to the actual data structure of your file.
data.columns = ['time', 'CH1', 'CH2',]
time=data["time"]
ch1=data["CH1"]
ch2=data["CH2"]

x = np.linspace(1, 9000,1000 )
y = 561/np.sqrt(561**2+1/((2*np.pi*x*90*10**(-9))**2))
#y_0 = 569/np.sqrt(569**2+1/((2*np.pi*x*85*10**(-9))**2))
y_1 = 553/np.sqrt(553**2+1/((2*np.pi*x*85*10**(-9))**2))
#y_2 = 569/np.sqrt(569**2+1/((2*np.pi*x*95*10**(-9))**2))

w = 2 * np.pi * 3000  # Omega (Kreisfrequenz, z.B. für 50 Hz)
t = np.linspace(-0.00035, 0.00035, 50000)  # Zeitachse von -20ms bis 20ms

# Die Fourier-Reihe inklusive dem Term der nächsten ungeraden Ordnung (7. Ordnung)
rechteck_signal = (4 *5/np.pi) *(0.333139*np.sin(w * t)
                    +0.256108*(1 / 3) * np.sin(3 * w * t)
                   +0.183779*(1 / 5) * np.sin(5 * w * t)
                   +0.13969*(1 / 7) * np.sin(7 * w * t)
                    +0.11172*(1 / 9) * np.sin(9 * w * t)
                   +0.092761*(1 / 11) * np.sin(11 * w * t)
                    +0.079172*(1/13) * np.sin(13 * w * t))  # Dieser Term kam neu hinzu)

rechteck_signal_u = (4 *5/np.pi) *(np.sin(w * t)
                    +(1 / 3) * np.sin(3 * w * t)
                   +(1 / 5) * np.sin(5 * w * t)
                   +(1 / 7) * np.sin(7 * w * t)
                    +(1 / 9) * np.sin(9 * w * t)
                   +(1 / 11) * np.sin(11 * w * t)
                    +(1/13) * np.sin(13 * w * t))  # Dieser Term kam neu hinzu)

fig, ax = plt.subplots(figsize=(8, 6))

#print(adcSorted)
#ax.scatter(x, y, label="CH2", s=5)
#ax.scatter(x, y_0, label="CH20", s=2)
#ax.scatter(x, y_1, label="CH21", s=5)
#ax.scatter(x, y_2, label="CH22", s=5)
#ax.scatter(time*1000, ch1, label="CH1", s=20)
ax.scatter(time*1000, ch1-5, label="CH1", s=20)
ax.scatter(time*1000, ch2, label="CH2", s=20)
ax.scatter(t*1000, rechteck_signal, label="CH3", s=2)
ax.scatter(t*1000, rechteck_signal_u, label="CH3", s=2)
#plt.hlines(0.707, xmin=0, xmax=9000, colors='black', linestyles='--')

#ax.scatter(time*1000, difference, label="Spannung", s=10)
ax.set_ylim(-8,8)
ax.set_xlabel("Zeit t/ms")
ax.set_ylabel("Spannung U/V")
#ax.hist(data["adc"], bins=100, color="royalblue", edgecolor="black", log=True)
# Filtert alle Werte unter 100 einfach heraus
# Neues Histogramm nur mit den hohen Signalen plottem
#ax.legend()
plt.grid(True)
plt.savefig("images/rechteck_3k.png") #zuerst save dann show
plt.show()

