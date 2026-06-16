import numpy as np

# Gegebene Konstanten definieren
R = 560              # Widerstand in Ohm
C = 90 * 10**(-9)    # Kapazität: 90 nF = 90 * 10^-9 Farad
w = 2 * np.pi * 3000
# Beispiel für w (falls w ein NumPy-Array oder ein einzelner Wert ist)
# w = 2 * np.pi * 3000

# Die Formel exakt nachgebaut:
# V = 1 / sqrt( 9 + ((w^2 * R^2 * C^2 - 1)^2) / (w^2 * R^2 * C^2) )

# Um Schreibfehler zu vermeiden, berechnen wir den wiederkehrenden Teil (w * R * C) im Voraus:
wRC = w * R * C
for i in range(1, 15, 2):
    V = 1 / np.sqrt(9 + ((i*wRC)**2 - 1)**2 / ((i*wRC)**2))
    print(i, V)