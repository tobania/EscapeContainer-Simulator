# EscapeContainer-Simulator

Scripts to help simulate the communication between the session manager and the various Physical devices.

# How to use

1. Simply clone this project,
2. Startup the MQTT Broker by executing the following command:

```ps1
docker-compose -
```

3. whether you need to simulate things for a challenge or a Actuator choose the correct file:

- Actuator

  _this is not yet available_

- Challenge

```ps1
python3 challenge-simulator.py
```

4. Follow the instructions which are prompted by the script.
