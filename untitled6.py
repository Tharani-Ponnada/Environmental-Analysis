import numpy as np
import pandas as pd

# Define the directory where you want to save the CSV files
save_directory = r"C:\Users\thara\Downloads\A2_CM402"  # Change this to your preferred directory

# Load and convert Delhi data to CSV
Delhi_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_temperature_1000hpa.npy")
Delhi_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_specifichumidity_1000hpa.npy")
Delhi_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Delhi_relativehumidity_1000hpa.npy")

df_delhi_temp = pd.DataFrame(Delhi_temperature)
df_delhi_sh = pd.DataFrame(Delhi_specific_humidity)
df_delhi_rh = pd.DataFrame(Delhi_relative_humidity)

df_delhi_temp.to_csv(f"{save_directory}\\Delhi_temperature.csv", index=False)
df_delhi_sh.to_csv(f"{save_directory}\\Delhi_specific_humidity.csv", index=False)
df_delhi_rh.to_csv(f"{save_directory}\\Delhi_relative_humidity.csv", index=False)

# Load and convert Jaipur data to CSV
Jaipur_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_temperature_1000hpa.npy")
Jaipur_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_specifichumidity_1000hpa.npy")
Jaipur_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jaipur_relativehumidity_1000hpa.npy")

df_jaipur_temp = pd.DataFrame(Jaipur_temperature)
df_jaipur_sh = pd.DataFrame(Jaipur_specific_humidity)
df_jaipur_rh = pd.DataFrame(Jaipur_relative_humidity)

df_jaipur_temp.to_csv(f"{save_directory}\\Jaipur_temperature.csv", index=False)
df_jaipur_sh.to_csv(f"{save_directory}\\Jaipur_specific_humidity.csv", index=False)
df_jaipur_rh.to_csv(f"{save_directory}\\Jaipur_relative_humidity.csv", index=False)

# Load and convert Jhunjhunu data to CSV
Jhunjhunu_temperature = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_temperature_1000hpa.npy")
Jhunjhunu_specific_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_specifichumidity_1000hpa.npy")
Jhunjhunu_relative_humidity = np.load(r"C:\Users\thara\Downloads\A2_CM402\Jhunjhunu_relativehumidity_1000hpa.npy")

df_jhunjhunu_temp = pd.DataFrame(Jhunjhunu_temperature)
df_jhunjhunu_sh = pd.DataFrame(Jhunjhunu_specific_humidity)
df_jhunjhunu_rh = pd.DataFrame(Jhunjhunu_relative_humidity)

df_jhunjhunu_temp.to_csv(f"{save_directory}\\Jhunjhunu_temperature.csv", index=False)
df_jhunjhunu_sh.to_csv(f"{save_directory}\\Jhunjhunu_specific_humidity.csv", index=False)
df_jhunjhunu_rh.to_csv(f"{save_directory}\\Jhunjhunu_relative_humidity.csv", index=False)
