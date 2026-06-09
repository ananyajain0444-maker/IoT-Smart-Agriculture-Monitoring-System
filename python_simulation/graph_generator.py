import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("images", exist_ok=True)

try:
    df = pd.read_csv("data/sensor_data.csv")

    plt.figure(figsize=(8, 4))
    plt.plot(df["Soil_Moisture"])
    plt.title("Soil Moisture Trend")
    plt.savefig("images/moisture_trend.png")
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(df["Temperature"])
    plt.title("Temperature Trend")
    plt.savefig("images/temperature_trend.png")
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(df["Humidity"])
    plt.title("Humidity Trend")
    plt.savefig("images/humidity_trend.png")
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(df["Light_Intensity"])
    plt.title("Light Intensity Trend")
    plt.savefig("images/light_intensity_trend.png")
    plt.close()

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.plot(df["Temperature"])
    plt.title("Temperature")

    plt.subplot(2, 2, 2)
    plt.plot(df["Humidity"])
    plt.title("Humidity")

    plt.subplot(2, 2, 3)
    plt.plot(df["Soil_Moisture"])
    plt.title("Soil Moisture")

    plt.subplot(2, 2, 4)
    plt.plot(df["Light_Intensity"])
    plt.title("Light Intensity")

    plt.tight_layout()
    plt.savefig("images/dashboard_summary.png")
    plt.close()

    print("All 5 images generated successfully!")

except Exception as e:
    print("Error:", e)