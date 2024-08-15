import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Define a function to plot trends
def plot_trends(data, title, y_label, output_filename):
    plt.figure(figsize=(12, 6))

    # Calculate the trend
    slope, _, _, _, _ = linregress(range(len(data)), data)

    # Plot the data
    plt.plot(range(len(data)), data, label="Data")
    trend = slope * np.array(range(len(data)))
    plt.plot(range(len(data)), trend, label=f'Trend ({y_label})')

    plt.xlabel("Time")
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.grid(True)

    # Save or display the plot
    plt.savefig(output_filename)
    plt.show()

# Load data for Delhi
Delhi_specific_humidity = np.load("C:/Users/thara/Downloads/Assignment 3/Delhi_specifichumidity_1000hpa.npy")
Delhi_temperature = np.load("C:/Users/thara/Downloads/Assignment 3/Delhi_temperature_1000hpa.npy")
Delhi_relative_humidity = pd.read_csv("C:/Users/thara/Downloads/Assignment 3/Delhi_relative_humidity.csv")["0"]
Delhi_precip = pd.read_csv("C:/Users/thara/Downloads/Assignment 3/Delhi_precip.csv")["0"]

# Plot trends for Delhi
plot_trends(Delhi_specific_humidity, "Trends in Delhi - Specific Humidity", "Specific Humidity", "Delhi_trends_specific_humidity.png")
plot_trends(Delhi_temperature, "Trends in Delhi - Temperature", "Temperature", "Delhi_trends_temperature.png")
plot_trends(Delhi_relative_humidity, "Trends in Delhi - Relative Humidity", "Relative Humidity", "Delhi_trends_relative_humidity.png")
plot_trends(Delhi_precip, "Trends in Delhi - Precipitation", "Precipitation", "Delhi_trends_precipitation.png")

# Load data for Jaipur
Jaipur_specific_humidity = np.load("C:/Users/thara/Downloads/Assignment 3/Jaipur_specifichumidity_1000hpa.npy")
Jaipur_temperature = np.load("C:/Users/thara/Downloads/Assignment 3/Jaipur_temperature_1000hpa.npy")
Jaipur_relative_humidity = pd.read_csv("C:/Users/thara/Downloads/Assignment 3/Jaipur_relative_humidity.csv")["0"]
Jaipur_precip = pd.read_csv("C:/Users/thara/Downloads/Assignment 3/Jaipur_precip.csv")["0"]

# Plot trends for Jaipur
plot_trends(Jaipur_specific_humidity, "Trends in Jaipur - Specific Humidity", "Specific Humidity", "Jaipur_trends_specific_humidity.png")
plot_trends(Jaipur_temperature, "Trends in Jaipur - Temperature", "Temperature", "Jaipur_trends_temperature.png")
plot_trends(Jaipur_relative_humidity, "Trends in Jaipur - Relative Humidity", "Relative Humidity", "Jaipur_trends_relative_humidity.png")
plot_trends(Jaipur_precip, "Trends in Jaipur - Precipitation", "Precipitation", "Jaipur_trends_precipitation.png")

# Load data for Jhunjhunu
Jhunjhunu_specific_humidity = np.load("C:/Users/thara/Downloads/Assignment 3/Jhunjhunu_specifichumidity_1000hpa.npy")
Jhunjhunu_temperature = np.load("C:/Users/thara/Downloads/Assignment 3/Jhunjhunu_temperature_1000hpa.npy")
Jhunjhunu_relative_humidity = pd.read_csv("C:/Users/thara/Downloads/Assignment 3/Jhunjhunu_relative_humidity.csv")["0"]
Jhunjhunu_precip = pd.read_csv("C:/Users/thara/Downloads/Assignment 3/Jhunjhunu_precip.csv")["0"]

# Plot trends for Jhunjhunu
plot_trends(Jhunjhunu_specific_humidity, "Trends in Jhunjhunu - Specific Humidity", "Specific Humidity", "Jhunjhunu_trends_specific_humidity.png")
plot_trends(Jhunjhunu_temperature, "Trends in Jhunjhunu - Temperature", "Temperature", "Jhunjhunu_trends_temperature.png")
plot_trends(Jhunjhunu_relative_humidity, "Trends in Jhunjhunu - Relative Humidity", "Relative Humidity", "Jhunjhunu_trends_relative_humidity.png")
plot_trends(Jhunjhunu_precip, "Trends in Jhunjhunu - Precipitation", "Precipitation", "Jhunjhunu_trends_precipitation.png")
