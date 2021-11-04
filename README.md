# EscapeContainer-Simulator

Scripts to help simulate the communication between the session manager and the various Physical devices.

# How to use

1. Simply clone this project,
2. Startup the MQTT Broker by executing the following command:

```ps1
docker-compose up
```

3. Install all dependencies using Pip(3):

```ps1
pip3 install paho-mqtt
```

4. whether you need to simulate things for a challenge or a Actuator choose the correct file:

- Actuator

  _this is not yet available_

- Challenge

```ps1
python3 challenge-simulator.py
```

5. Follow the instructions which are prompted by the script.
