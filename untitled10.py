import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data for Delhi, Jaipur, and Jhunjhunu
delhi_precip = np.load(r"C:\Users\thara\Downloads\Assignment 3\Delhi_precip.npy")
jaipur_precip = np.load(r"C:\Users\thara\Downloads\Assignment 3\Jaipur_precip.npy")
jhunjhunu_precip = np.load(r"C:\Users\thara\Downloads\Assignment 3\Jhunjhunu_precip.npy")

# Function to calculate trends
def calculate_trends(data, y_label, region_name):
    # Create an array of years as the x-axis
    years = np.arange(1971, 1971 + len(data))  # Adjust the start year as needed

    # Calculate trends for the given data
    trends = []
    for i in range(len(data)):
        start = i - 91  # June 1st
        end = i - 1  # September 30th
        if start < 0:
            trend = 0  # Not enough data points
        else:
            trend = np.mean(data[start:end + 1])
        trends.append(trend)

    # Plot the trends
    plt.figure(figsize=(10, 5))
    plt.plot(years, trends, label=f'Trend ({y_label})')
    plt.title(f"Trends in {region_name} - {y_label} (June-September)")
    plt.xlabel("Year")
    plt.ylabel(f"{y_label} Trend")
    plt.legend()
    plt.grid()
    plt.savefig(f"{region_name}_trends_{y_label}.png")

# Calculate and plot trends for Delhi
calculate_trends(delhi_precip, 'Precipitation', 'Delhi')

# Calculate and plot trends for Jaipur
calculate_trends(jaipur_precip, 'Precipitation', 'Jaipur')

# Calculate and plot trends for Jhunjhunu
calculate_trends(jhunjhunu_precip, 'Precipitation', 'Jhunjhunu')

plt.show()
