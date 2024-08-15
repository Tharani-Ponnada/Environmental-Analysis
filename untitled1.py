import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Define a function to resample data
def resample_data(data, new_length):
    resampled_data = []
    for i in range(0, len(data), len(data) // new_length):
        resampled_data.append(data[i:i + len(data) // new_length])
    return np.array(resampled_data)

# Load specific humidity and relative humidity data for Delhi
Delhi_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_specifichumidity_1000hpa.npy")
Delhi_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_relativehumidity_1000hpa.npy")

# Load specific humidity and relative humidity data for Jaipur
Jaipur_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_specifichumidity_1000hpa.npy")
Jaipur_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_relativehumidity_1000hpa.npy")

# Load specific humidity and relative humidity data for Jhunjhunu
Jhunjhunu_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_specifichumidity_1000hpa.npy")
Jhunjhunu_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_relativehumidity_1000hpa.npy")

# Find the minimum length of data
min_length = min(len(Delhi_specific_humidity), len(Jaipur_specific_humidity), len(Jhunjhunu_specific_humidity),
                 len(Delhi_relative_humidity), len(Jaipur_relative_humidity), len(Jhunjhunu_relative_humidity))

# Resample data to have the same length
new_length = min_length
Delhi_specific_humidity = resample_data(Delhi_specific_humidity, new_length)
Delhi_relative_humidity = resample_data(Delhi_relative_humidity, new_length)

Jaipur_specific_humidity = resample_data(Jaipur_specific_humidity, new_length)
Jaipur_relative_humidity = resample_data(Jaipur_relative_humidity, new_length)

Jhunjhunu_specific_humidity = resample_data(Jhunjhunu_specific_humidity, new_length)
Jhunjhunu_relative_humidity = resample_data(Jhunjhunu_relative_humidity, new_length)

# Calculate annual mean values for specific humidity and relative humidity
annual_mean_delhi_specific_humidity = np.nanmean(Delhi_specific_humidity.reshape((365, -1), order='F'), axis=0)
annual_mean_delhi_relative_humidity = np.nanmean(Delhi_relative_humidity.reshape((365, -1), order='F'), axis=0)

annual_mean_jaipur_specific_humidity = np.nanmean(Jaipur_specific_humidity.reshape((365, -1), order='F'), axis=0)
annual_mean_jaipur_relative_humidity = np.nanmean(Jaipur_relative_humidity.reshape((365, -1), order='F'), axis=0)

annual_mean_jhunjhunu_specific_humidity = np.nanmean(Jhunjhunu_specific_humidity.reshape((365, -1), order='F'), axis=0)
annual_mean_jhunjhunu_relative_humidity = np.nanmean(Jhunjhunu_relative_humidity.reshape((365, -1), order='F'), axis=0)

# Perform trend analysis
# Delhi
slope_delhi_sh, _, _, _, _ = linregress(range(1970, 1970 + new_length), annual_mean_delhi_specific_humidity)
slope_delhi_rh, _, _, _, _ = linregress(range(1970, 1970 + new_length), annual_mean_delhi_relative_humidity)

# Jaipur
slope_jaipur_sh, _, _, _, _ = linregress(range(1970, 1970 + new_length), annual_mean_jaipur_specific_humidity)
slope_jaipur_rh, _, _, _, _ = linregress(range(1970, 1970 + new_length), annual_mean_jaipur_relative_humidity)

# Jhunjhunu
slope_jhunjhunu_sh, _, _, _, _ = linregress(range(1970, 1970 + new_length), annual_mean_jhunjhunu_specific_humidity)
slope_jhunjhunu_rh, _, _, _, _ = linregress(range(1970, 1970 + new_length), annual_mean_jhunjhunu_relative_humidity)

# Plot trends
plt.figure(figsize=(16, 6))

# Delhi
plt.subplot(2, 3, 1)
plt.plot(range(1970, 1970 + new_length), annual_mean_delhi_specific_humidity, color='blue', marker='o')
plt.title('Delhi Specific Humidity Trend')
plt.xlabel('Year')
plt.ylabel('Specific Humidity')
plt.xticks(range(1970, 1970 + new_length, 10), rotation=45)
plt.grid(True)
plt.axhline(y=annual_mean_delhi_specific_humidity[0], color='gray', linestyle='--', label='Baseline')
plt.text(2000, annual_mean_delhi_specific_humidity[0], f'Slope: {slope_delhi_sh:.4f}', color='red')
plt.legend()

plt.subplot(2, 3, 4)
plt.plot(range(1970, 1970 + new_length), annual_mean_delhi_relative_humidity, color='blue', marker='o')
plt.title('Delhi Relative Humidity Trend')
plt.xlabel('Year')
plt.ylabel('Relative Humidity')
plt.xticks(range(1970, 1970 + new_length, 10), rotation=45)
plt.grid(True)
plt.axhline(y=annual_mean_delhi_relative_humidity[0], color='gray', linestyle='--', label='Baseline')
plt.text(2000, annual_mean_delhi_relative_humidity[0], f'Slope: {slope_delhi_rh:.4f}', color='red')
plt.legend()

# Jaipur
plt.subplot(2, 3, 2)
plt.plot(range(1970, 1970 + new_length), annual_mean_jaipur_specific_humidity, color='green', marker='o')
plt.title('Jaipur Specific Humidity Trend')
plt.xlabel('Year')
plt.ylabel('Specific Humidity')
plt.xticks(range(1970, 1970 + new_length, 10), rotation=45)
plt.grid(True)
plt.axhline(y=annual_mean_jaipur_specific_humidity[0], color='gray', linestyle='--', label='Baseline')
plt.text(2000, annual_mean_jaipur_specific_humidity[0], f'Slope: {slope_jaipur_sh:.4f}', color='red')
plt.legend()

plt.subplot(2, 3, 5)
plt.plot(range(1970, 1970 + new_length), annual_mean_jaipur_relative_humidity, color='green', marker='o')
plt.title('Jaipur Relative Humidity Trend')
plt.xlabel('Year')
plt.ylabel('Relative Humidity')
plt.xticks(range(1970, 1970 + new_length, 10), rotation=45)
plt.grid(True)
plt.axhline(y=annual_mean_jaipur_relative_humidity[0], color='gray', linestyle='--', label='Baseline')
plt.text(2000, annual_mean_jaipur_relative_humidity[0], f'Slope: {slope_jaipur_rh:.4f}', color='red')
plt.legend()

# Jhunjhunu
plt.subplot(2, 3, 3)
plt.plot(range(1970, 1970 + new_length), annual_mean_jhunjhunu_specific_humidity, color='orange', marker='o')
plt.title('Jhunjhunu Specific Humidity Trend')
plt.xlabel('Year')
plt.ylabel('Specific Humidity')
plt.xticks(range(1970, 1970 + new_length, 10), rotation=45)
plt.grid(True)
plt.axhline(y=annual_mean_jhunjhunu_specific_humidity[0], color='gray', linestyle='--', label='Baseline')
plt.text(2000, annual_mean_jhunjhunu_specific_humidity[0], f'Slope: {slope_jhunjhunu_sh:.4f}', color='red')
plt.legend()

plt.subplot(2, 3, 6)
plt.plot(range(1970, 1970 + new_length), annual_mean_jhunjhunu_relative_humidity, color='orange', marker='o')
plt.title('Jhunjhunu Relative Humidity Trend')
plt.xlabel('Year')
plt.ylabel('Relative Humidity')
plt.xticks(range(1970, 1970 + new_length, 10), rotation=45)
plt.grid(True)
plt.axhline(y=annual_mean_jhunjhunu_relative_humidity[0], color='gray', linestyle='--', label='Baseline')
plt.text(2000, annual_mean_jhunjhunu_relative_humidity[0], f'Slope: {slope_jhunjhunu_rh:.4f}', color='red')
plt.legend()

plt.tight_layout()

# Show the plots
plt.show()
