def control_pump(soil_moisture):

    moisture_threshold = 30

    if soil_moisture < moisture_threshold:
        return "ON"
    else:
        return "OFF"