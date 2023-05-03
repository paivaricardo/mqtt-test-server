import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, result_code):
    print("Connected to the MQTT instance with the result code", str(result_code))
    client.subscribe("test/topic")


def on_message(client, userdata, msg):
    print("{" + msg.topic + "} " + str(msg.payload))


if __name__ == '__main__':
    # MQTT client instance
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Conectar à instância MQTT na porta 1883
    client.connect("18.214.223.254", 1883, 60)
    client.loop_start()

    # Publicar a mensagem Hello, world na porta 1883
    client.publish("planto-iot-sensores", "Hello, world!")

    client.loop_stop()
    client.disconnect()
