import time

import paho.mqtt.client as mqtt

#############################
### Configuration Section ###
#############################
ChallengeReference = "0d3d6876-c8c5-4f89-af4d-057c6ae9dcbc"
MqttHost = "127.0.0.1"
SimulatorClientId = "ChallengeSimulator"

##########################################################################################################################################################

#########################################
### Topic configration - don't change ###
#########################################
ChallengeEventTopic = "challenges/event"
RegisterTopic = "challenges/registry"
ResetChallengeTopic = "challenges/" + ChallengeReference + "/reset"
RequestToRegisterTopic = "pd/requestregister"

########################
### Global variables ###
########################

Client: mqtt.Client = None

LastIncommingMessage: str = None

######################
### Helper methods ###
######################


def RegisterMqtt():
    global Client
    global ChallengeEventTopic
    global RegisterTopic
    global SimulatorClientId
    print("Registering to MQTT Broker...")
    Client = mqtt.Client(SimulatorClientId, clean_session=False)
    Client.message_callback_add(RegisterTopic, OnMessage)
    Client.message_callback_add(ChallengeEventTopic, OnMessage)
    Client.connect(MqttHost, port=1883, keepalive=60)
    Client.subscribe([(RegisterTopic, 2)], [(ChallengeEventTopic, 2)])
    Client.loop_start()
    print("MQTT Ready!")


def OnMessage(client, userdata, message: mqtt.MQTTMessage):
    global LastIncommingMessage
    payload = message.payload.decode("utf-8")
    print(
        "\n[!] Received message on topic"
        + message.topic
        + ", with payload: "
        + payload
        + "\n"
    )


def ShowMenu():
    print()
    print("Tobania.EscapeContainer Challenge Simulator v1.0")
    print(
        "This tool will keep listening on the MQTT Topics ChallengeEventTopic and RegisterTopic and print the output of the messages.\n"
        + " You can then submit messages to other topics, using the following menu"
    )
    print("Options:")
    print("1: Send RequestToRegister")
    print("2: Send ResetChallenge")
    print("0: Refresh this menu")
    print("hit any other key to terminate the simulator")


def SendToTopic(topicName: str, payload: str):
    global Client
    if Client.is_connected:
        Client.publish(topicName, payload)


def SendRequestToRegister():
    global RequestToRegisterTopic
    print("Sending Request to register...")
    SendToTopic(RequestToRegisterTopic, "RequestToRegister")


def SendResetChallenge():
    global ResetChallengeTopic
    resetPayload = input("[?] Please enter the reset payload to send: ")
    if resetPayload is not None and resetPayload != "":
        SendToTopic(ResetChallengeTopic, resetPayload)


# Main method
def main():
    global ChallengeReference
    global Client
    global LastIncommingMessage
    print("Starting Challenge Simulator with parameters:")
    print("\t- " + ChallengeReference)
    RegisterMqtt()

    while True:
        ShowMenu()
        command = input("[?] What do you want to do? ")
        if command == "1":
            SendRequestToRegister()
            print("-----------")
        elif command == "2":
            SendResetChallenge()
            print("-----------")
        elif command == "0":
            print("-----------")
        else:
            print("Terminating simulator")
            break
    Client.loop_stop()
    Client.disconnect()


# Start logic
if __name__ == "__main__":
    main()
