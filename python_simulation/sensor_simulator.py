import random
from datetime import datetime

def generate_sensor_data():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(20, 40), 2),
        "humidity": round(random.uniform(30, 90), 2),
        "soil_moisture": round(random.uniform(10, 100), 2),
        "light_intensity": random.randint(100, 1000)
    }