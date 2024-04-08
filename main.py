import matplotlib.pyplot as plt

# Laden der Daten
from load_data import sorted_power_W

# Plotte mir eine Liste mit Matplotlib
plt.plot(sorted_power_W[::-1])
plt.xlabel('Dauerlinie in Sekunden')
plt.ylabel('Power in Watt')
plt.show()