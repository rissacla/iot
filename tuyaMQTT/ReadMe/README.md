How to setup:
1) cd inside tuya-mqtt to run in terminal:
node tuya-mqtt.js
2) Run Mosquitto in another seperate terminal
mosquitto -c mosquitto.conf -v
3) Run in /mos2 in another seperate terminal
./mosquitto_sub -h 192.168.86.22 -t "tuya/smart_plug_2/DPS/1/state"

Setup tuya-mqtt
1) go into tuyaMQTT folder in terminal
git clone https://github.com/TheAgentK/tuya-mqtt

// change directory to the project directory
cd tuya-mqtt

//installs this project along with codetheweb/tuyapi project
npm install
2) write in terminal
cp config.json.sample config.json

