import os
import random
import time

duration = 5 * 60 * 60  # 5 hours in seconds

start_time = time.time()

while (time.time() - start_time) < duration:
    # ----------------------------------------------Station 1--------------------------------------
    # Generate random values for each sensor in the station 1
    temperature = random.randint(-50, 50)
    humidity = random.randint(0, 100)
    co2sensor = random.randint(300, 2000)
    rain_height = random.randint(0, 50)
    wind_direction = random.randint(0, 360)
    wind_intensity = random.randint(0, 100)

    # Temperature Sensor
    temp1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "TDfLWYErdzJhCv6WGSLw" -m {{"temperature":{temperature}}}'
    os.system(temp1)

    # Humidity Sensor
    humidity1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "lQLeRsfGEvYJWfVFgkd9" -m {{"humidity":{humidity}}}'
    os.system(humidity1)

    # Co2 Sensor
    co2_1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "OReGm52q8gMOmK7bXpq4" -m {{"co2sensor":{co2sensor}}}'
    os.system(co2_1)

    # Rain Sensor
    rain_sensor = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "kijE1Zs5IbOjo2rqS1kh" -m {{"rain_height":{rain_height}}}'
    os.system(rain_sensor)

    # Wind Direction Sensor
    wind_direction = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "5qRPx0MoUCJaxJWKveCN" -m {{"wind_direction":{wind_direction}}}'
    os.system(wind_direction)

    # Wind Intensity Sensor
    wind_intensity = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "YTujXyhGKOvlYMow7YlO" -m {{"wind_intensity":{wind_intensity}}}'
    os.system(wind_intensity)

    # ---------------------------------------Station 2----------------------------------
    # Generate random values for each sensor in the station 2
    temperature = random.randint(-50, 50)
    humidity = random.randint(0, 100)
    co2sensor = random.randint(300, 2000)
    rain_height = random.randint(0, 50)
    wind_direction = random.randint(0, 360)
    wind_intensity = random.randint(0, 100)

    # Temperature Sensor
    temp1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "aTpywXiH6EIYXYY6N0og" -m {{"temperature":{temperature}}}'
    os.system(temp1)

    # Humidity Sensor
    humidity1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "bSP1hycbLVt52qMDon9C" -m {{"humidity":{humidity}}}'
    os.system(humidity1)

    # Co2 Sensor
    co2_1 = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "eP9K5gezmEGS9LCxOo9J" -m {{"co2sensor":{co2sensor}}}'
    os.system(co2_1)

    # Rain Sensor
    rain_sensor = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "bjdAuIoyFPtSFNv4JQnm" -m {{"rain_height":{rain_height}}}'
    os.system(rain_sensor)

    # Wind Direction Sensor
    wind_direction = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "yzcGRHjKi4eq3BdPelRY" -m {{"wind_direction":{wind_direction}}}'
    os.system(wind_direction)

    # Wind Intensity Sensor
    wind_intensity = f'mosquitto_pub -d -q 1 -h "demo.thingsboard.io" -p "1883" -t "v1/devices/me/telemetry" -u "XRI7qvZ1LjVQtkVM7V0H" -m {{"wind_intensity":{wind_intensity}}}'
    os.system(wind_intensity)

    # Time between each message
    time.sleep(10)
