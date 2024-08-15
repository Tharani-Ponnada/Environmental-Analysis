import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# List of region names
regions = ["Delhi", "Jaipur", "Jhunjhunu"]

def calculate_seasonal_cycle_and_variability(data, region_name):
    # Assuming the data is organized as [precipitation1, precipitation2, ...] with no date information
    data = pd.DataFrame(data, columns=["precipitation"])
    
    # Create an index based on the number of data points
    data['date'] = pd.date_range(start="1970-01-01", periods=len(data), freq="D")
    
    # Set the date column as the index
    data.set_index('date', inplace=True)

    # Calculate the seasonal cycle of precipitation
    seasonal_cycle = data.groupby(data.index.dayofyear)['precipitation'].mean()

    # Calculate the standard deviation of daily precipitation
    precipitation_std = data.groupby(data.index.dayofyear)['precipitation'].std()

    # Plot the seasonal cycle of precipitation and its standard deviation
    plt.figure(figsize=(12, 6))
    plt.plot(seasonal_cycle, label='Seasonal Cycle', color='blue')
    plt.fill_between(
        seasonal_cycle.index,
        seasonal_cycle - precipitation_std,
        seasonal_cycle + precipitation_std,
        alpha=0.3,
        label='Standard Deviation',
        color='orange'
    )

    plt.title(f'Seasonal Cycle and Variability of Precipitation in {region_name}')
    plt.xlabel('Day of Year')
    plt.ylabel('Precipitation')
    plt.legend()
    plt.show()

# Loop through each region's data
for region_name in regions:
    # Load the data for the respective region
    data = np.load(f"C:/Users/thara/Downloads/Assignment 3/{region_name}_precip.npy")
    
    # Calculate and plot seasonal cycle and variability
    calculate_seasonal_cycle_and_variability(data, region_name)
