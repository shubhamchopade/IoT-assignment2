# CIS600 Internet of Things: Application Development

## Spring 2023 - Assignment 2

## About the project

The python script consists of runs a loop for a duration of 5 hours and send the data to the MQTT server hosted at demo.thingsboard.io. The data is randomly generated using the random library in python. The data is sent every 5 seconds to the MQTT server and can be viewed on the telemetry tab of the device on thingsboard.io. The script can be modified to send the data to any MQTT server by changing the MQTT_SERVER_HOST, ACCESS_TOKEN and PORT.

`mosquitto_pub -d -q 1 -h "MQTT_SERVER_HOST" -p "PORT" -t "TELEMETRY" -u "ACCESS_TOKEN" -m "DATA"`

## Requirements:</b>

1. Python 3.6 or above
2. MQTT Client (mosquitto for MacOS)
3. Setup a demo account on [thingsboard.io](demo.thingsboard.io)
4. Get the access token from the thingsboard.io for the device you want to send the data to.

---

## Installation steps for MacOS:</b>

1. Install musquitto using the following command: `brew install mosquitto-clients`
2. Run the script using the following command: `python3 main.py`

---

## Once script is running:</b>

1. Login to thingsboard.io
2. Go to the device you want to see the data for.
3. Click on the telemetry tab and you should see the data being sent every 5 seconds.

## <b> Demo - Dashboard interface to monitor data from multiple devices</b>

## Station 1

![Station 1](https://pico.techsapien.dev/!TMwoN9iEb7)

## Station 2

![Station 2](https://pico.techsapien.dev/!TNXYb3E3qZ)
