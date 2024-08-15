import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate trends
def calculate_trends(data, y_label):
    # Calculate the trend
    length = len(data)
    slope = np.polyfit(range(length), data, 1)[0]
    trend = slope * np.array(range(length))

    return trend

# Function to plot trends
def plot_trends(data, title, y_label, save_path):
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(data)), data, label=y_label)
    plt.plot(range(len(data)), calculate_trends(data, y_label), label=f'Trend ({y_label})')
    plt.title(title)
    plt.xlabel("Time (Days)")
    plt.ylabel(y_label)
    plt.legend()
    plt.savefig(save_path)
    plt.show()

# Load data from CSV files
delhi_temperature = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Delhi_temperature.csv")['0']
jaipur_temperature = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Jaipur_temperature.csv")['0']
jhunjhunu_temperature = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Jhunjhunu_temperature.csv")['0']

delhi_specific_humidity = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Delhi_specific_humidity.csv")['0']
jaipur_specific_humidity = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Jaipur_specific_humidity.csv")['0']
jhunjhunu_specific_humidity = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Jhunjhunu_specific_humidity.csv")['0']

delhi_relative_humidity = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Delhi_relative_humidity.csv")['0']
jaipur_relative_humidity = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Jaipur_relative_humidity.csv")['0']
jhunjhunu_relative_humidity = pd.read_csv(r"C:\Users\thara\Downloads\Assignment 3\Jhunjhunu_relative_humidity.csv")['0']

# Plot trends for temperature
plot_trends(delhi_temperature, "Trends in Delhi - Temperature", "Temperature", "Delhi_trends_temperature.png")
plot_trends(jaipur_temperature, "Trends in Jaipur - Temperature", "Temperature", "Jaipur_trends_temperature.png")
plot_trends(jhunjhunu_temperature, "Trends in Jhunjhunu - Temperature", "Temperature", "Jhunjhunu_trends_temperature.png")

# Plot trends for specific humidity
plot_trends(delhi_specific_humidity, "Trends in Delhi - Specific Humidity", "Specific Humidity", "Delhi_trends_specific_humidity.png")
plot_trends(jaipur_specific_humidity, "Trends in Jaipur - Specific Humidity", "Specific Humidity", "Jaipur_trends_specific_humidity.png")
plot_trends(jhunjhunu_specific_humidity, "Trends in Jhunjhunu - Specific Humidity", "Specific Humidity", "Jhunjhunu_trends_specific_humidity.png")

# Plot trends for relative humidity
plot_trends(delhi_relative_humidity, "Trends in Delhi - Relative Humidity", "Relative Humidity", "Delhi_trends_relative_humidity.png")
plot_trends(jaipur_relative_humidity, "Trends in Jaipur - Relative Humidity", "Relative Humidity", "Jaipur_trends_relative_humidity.png")
plot_trends(jhunjhunu_relative_humidity, "Trends in Jhunjhunu - Relative Humidity", "Relative Humidity", "Jhunjhunu_trends_relative_humidity.png")
