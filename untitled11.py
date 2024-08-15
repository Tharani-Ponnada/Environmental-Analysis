import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define a function to calculate linear trends
def calculate_trends(data, y_label, region_name):
    df = pd.DataFrame({'Date': date_range, y_label: data})
    df['Year'] = df['Date'].dt.year
    grouped = df.groupby('Year').mean()
    grouped.reset_index(inplace=True)

    # Calculate the linear trend
    x = grouped.index
    y = grouped[y_label]
    slope, intercept = np.polyfit(x, y, 1)
    trend_line = slope * x + intercept

    # Plot the data and trend
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'{y_label} Trend')
    plt.plot(x, trend_line, label=f'Trend ({y_label})', linestyle='--', color='red')
    plt.xlabel('Year')
    plt.ylabel(y_label)
    plt.title(f'Trends in {region_name} - {y_label}')
    plt.legend()
    plt.savefig(f'{region_name}_trends_{y_label}.png')
    plt.show()

# Load CSV files
delhi_precip = pd.read_csv('C:/Users/thara/Downloads/Assignment 3/Delhi_precip.csv')
jaipur_precip = pd.read_csv('C:/Users/thara/Downloads/Assignment 3/Jaipur_precip.csv')
jhunjhunu_precip = pd.read_csv('C:/Users/thara/Downloads/Assignment 3/Jhunjhunu_precip.csv')

# Assuming your CSV files have a 'Date' column in a proper date format
date_range = pd.date_range(start='1970-01-01', periods=delhi_precip.shape[0], freq='D')

# Calculate trends for each region and variable
calculate_trends(delhi_precip['Precipitation'], 'Precipitation', 'Delhi')
calculate_trends(jaipur_precip['Precipitation'], 'Precipitation', 'Jaipur')
calculate_trends(jhunjhunu_precip['Precipitation'], 'Precipitation', 'Jhunjhunu')

# You can add more functions like calculate_trends for other variables and compare the trends.
