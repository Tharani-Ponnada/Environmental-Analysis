# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 02:28:54 2023

@author: thara
"""

import numpy as np
import matplotlib.pyplot as plt


# Load temperature and specific humidity data for Delhi, Jaipur, and Jhunjhunu
Delhi_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_temperature_1000hpa.npy")
Delhi_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_specifichumidity_1000hpa.npy")

Jaipur_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_temperature_1000hpa.npy")
Jaipur_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_specifichumidity_1000hpa.npy")

Jhunjhunu_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_temperature_1000hpa.npy")
Jhunjhunu_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_specifichumidity_1000hpa.npy")

# Rest of the code remains the same


# Plot specific humidity vs. temperature for Delhi
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.scatter(Delhi_temperature, Delhi_specific_humidity, color='blue', alpha=0.5)
plt.title('Delhi')
plt.xlabel('Temperature')
plt.ylabel('Specific Humidity')
plt.grid()

# Plot specific humidity vs. temperature for Jaipur
plt.subplot(1, 3, 2)
plt.scatter(Jaipur_temperature, Jaipur_specific_humidity, color='green', alpha=0.5)
plt.title('Jaipur')
plt.xlabel('Temperature')
plt.ylabel('Specific Humidity')
plt.grid()

# Plot specific humidity vs. temperature for Jhunjhunu
plt.subplot(1, 3, 3)
plt.scatter(Jhunjhunu_temperature, Jhunjhunu_specific_humidity, color='red', alpha=0.5)
plt.title('Jhunjhunu')
plt.xlabel('Temperature')
plt.ylabel('Specific Humidity')
plt.grid()

plt.tight_layout()
plt.show()
