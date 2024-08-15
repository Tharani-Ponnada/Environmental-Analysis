# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 02:34:57 2023

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

# Create scatter plots for specific humidity vs. temperature for all three regions
plt.figure(figsize=(15, 5))

# Plot for Delhi
plt.subplot(1, 3, 1)
plt.scatter(Delhi_temperature, Delhi_specific_humidity, color='blue', alpha=0.5)
plt.title('Specific Humidity vs. Temperature in Delhi')
plt.xlabel('Temperature (°C)')
plt.ylabel('Specific Humidity (g/kg)')
plt.grid()

# Plot for Jaipur
plt.subplot(1, 3, 2)
plt.scatter(Jaipur_temperature, Jaipur_specific_humidity, color='green', alpha=0.5)
plt.title('Specific Humidity vs. Temperature in Jaipur')
plt.xlabel('Temperature (°C)')
plt.ylabel('Specific Humidity (g/kg)')
plt.grid()

# Plot for Jhunjhunu
plt.subplot(1, 3, 3)
plt.scatter(Jhunjhunu_temperature, Jhunjhunu_specific_humidity, color='red', alpha=0.5)
plt.title('Specific Humidity vs. Temperature in Jhunjhunu')
plt.xlabel('Temperature (°C)')
plt.ylabel('Specific Humidity (g/kg)')
plt.grid()

plt.tight_layout()
plt.show()
