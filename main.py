import csv
import random
from datetime import datetime

with open("data/sensor_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Timestamp",
        "Temperature",
        "Humidity",
        "Soil_Moisture",
        "Light_Intensity",
        "Pump_Status"
    ])

    for i in range(30):

        temperature = round(random.uniform(20, 40), 2)
        humidity = round(random.uniform(30, 90), 2)
        soil = round(random.uniform(10, 100), 2)
        light = random.randint(100, 1000)

        pump = "ON" if soil < 30 else "OFF"

        writer.writerow([
            datetime.now(),
            temperature,
            humidity,
            soil,
            light,
            pump
        ])

print("30 sensor records generated successfully.")