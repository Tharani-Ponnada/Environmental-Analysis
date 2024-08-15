import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load temperature, specific humidity, and relative humidity data for all three regions
# Replace 'path_to_data_delhi', 'path_to_data_jaipur', 'path_to_data_jhunjhunu' with the actual file paths
Delhi_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_temperature_1000hpa.npy")
Delhi_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_specifichumidity_1000hpa.npy")
Delhi_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_relativehumidity_1000hpa.npy")

Jaipur_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_temperature_1000hpa.npy")
Jaipur_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_specifichumidity_1000hpa.npy")
Jaipur_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_relativehumidity_1000hpa.npy")

Jhunjhunu_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_temperature_1000hpa.npy")
Jhunjhunu_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_specifichumidity_1000hpa.npy")
Jhunjhunu_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_relativehumidity_1000hpa.npy")

# Define a function to find and plot seasonal peaks
def find_and_plot_seasonal_peaks(data, variable_name, region_name):
    peaks, _ = find_peaks(data, distance=150)  # Adjust the distance parameter as needed
    plt.figure(figsize=(12, 6))
    plt.plot(data, color='blue')
    plt.plot(peaks, data[peaks], "ro")
    plt.title(f"Seasonal Peaks of {variable_name} in {region_name}")
    plt.xlabel("Day of Year")
    plt.ylabel(variable_name)
    plt.grid()
    plt.show()

# Call the function for each variable and region
find_and_plot_seasonal_peaks(Delhi_temperature, "Temperature", "Delhi")
find_and_plot_seasonal_peaks(Delhi_specific_humidity, "Specific Humidity", "Delhi")
find_and_plot_seasonal_peaks(Delhi_relative_humidity, "Relative Humidity", "Delhi")

find_and_plot_seasonal_peaks(Jaipur_temperature, "Temperature", "Jaipur")
find_and_plot_seasonal_peaks(Jaipur_specific_humidity, "Specific Humidity", "Jaipur")
find_and_plot_seasonal_peaks(Jaipur_relative_humidity, "Relative Humidity", "Jaipur")

find_and_plot_seasonal_peaks(Jhunjhunu_temperature, "Temperature", "Jhunjhunu")
find_and_plot_seasonal_peaks(Jhunjhunu_specific_humidity, "Specific Humidity", "Jhunjhunu")
find_and_plot_seasonal_peaks(Jhunjhunu_relative_humidity, "Relative Humidity", "Jhunjhunu")
