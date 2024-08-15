import numpy as np
import matplotlib.pyplot as plt

def get_seasonality(data):
    ts_clim = data.reshape([365, -1], order='F')
    return np.nanmean(ts_clim, axis=1)

# Load specific humidity and relative humidity data for Delhi
Delhi_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_specifichumidity_1000hpa.npy")
Delhi_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_relativehumidity_1000hpa.npy")

# Load specific humidity and relative humidity data for Jaipur
Jaipur_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_specifichumidity_1000hpa.npy")
Jaipur_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_relativehumidity_1000hpa.npy")

# Load specific humidity and relative humidity data for Jhunjhunu
Jhunjhunu_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_specifichumidity_1000hpa.npy")
Jhunjhunu_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_relativehumidity_1000hpa.npy")

# Calculate seasonality for specific humidity and relative humidity
Delhi_specific_humidity_seasonality = get_seasonality(Delhi_specific_humidity)
Delhi_relative_humidity_seasonality = get_seasonality(Delhi_relative_humidity)

Jaipur_specific_humidity_seasonality = get_seasonality(Jaipur_specific_humidity)
Jaipur_relative_humidity_seasonality = get_seasonality(Jaipur_relative_humidity)

Jhunjhunu_specific_humidity_seasonality = get_seasonality(Jhunjhunu_specific_humidity)
Jhunjhunu_relative_humidity_seasonality = get_seasonality(Jhunjhunu_relative_humidity)

# Plot seasonality for specific humidity and relative humidity for all three regions
plt.figure(figsize=(12, 6))

# Plot for Delhi
plt.subplot(2, 3, 1)
plt.plot(Delhi_specific_humidity_seasonality)
plt.title('Delhi Specific Humidity Seasonality')
plt.xlabel('Day of Year')
plt.ylabel('Specific Humidity')

plt.subplot(2, 3, 4)
plt.plot(Delhi_relative_humidity_seasonality)
plt.title('Delhi Relative Humidity Seasonality')
plt.xlabel('Day of Year')
plt.ylabel('Relative Humidity')

# Plot for Jaipur
plt.subplot(2, 3, 2)
plt.plot(Jaipur_specific_humidity_seasonality)
plt.title('Jaipur Specific Humidity Seasonality')
plt.xlabel('Day of Year')
plt.ylabel('Specific Humidity')

plt.subplot(2, 3, 5)
plt.plot(Jaipur_relative_humidity_seasonality)
plt.title('Jaipur Relative Humidity Seasonality')
plt.xlabel('Day of Year')
plt.ylabel('Relative Humidity')

# Plot for Jhunjhunu
plt.subplot(2, 3, 3)
plt.plot(Jhunjhunu_specific_humidity_seasonality)
plt.title('Jhunjhunu Specific Humidity Seasonality')
plt.xlabel('Day of Year')
plt.ylabel('Specific Humidity')

plt.subplot(2, 3, 6)
plt.plot(Jhunjhunu_relative_humidity_seasonality)
plt.title('Jhunjhunu Relative Humidity Seasonality')
plt.xlabel('Day of Year')
plt.ylabel('Relative Humidity')

# Show the plots
plt.tight_layout()
plt.show()
