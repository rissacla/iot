How to setup:
1) cd inside tuya-mqtt to run in terminal:
node tuya-mqtt.js
2) Run Mosquitto in another seperate terminal
mosquitto -c mosquitto.conf -v
3) Run in /mos2 in another seperate terminal
./mosquitto_sub -h 192.168.86.22 -t "tuya/smart_plug_2/DPS/1/state"

