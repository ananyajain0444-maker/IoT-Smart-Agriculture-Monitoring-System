def generate_alerts(data):

    alerts = []

    if data["soil_moisture"] < 30:
        alerts.append("LOW SOIL MOISTURE ALERT")

    if data["temperature"] > 35:
        alerts.append("HIGH TEMPERATURE ALERT")

    if data["humidity"] < 40:
        alerts.append("LOW HUMIDITY ALERT")

    return alerts