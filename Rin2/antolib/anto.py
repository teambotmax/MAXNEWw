import antolib.AntoCommon
import paho.mqtt.client as mqtt

client = mqtt.Client()

class Anto():
    def __init__(self, user, key, thing):
        self.user = user
        self.key = key
        self.thing = thing
        self.mqtt = Mqtt(user, key, thing)
        client.username_pw_set(self.user, self.key)
        client.connect('service.anto.io', 1883, 60)
        #print('Created anto object!')

    def getVersion(self):
        return AntoCommon.ANTO_VER

    def sub(self, channel):
        #print('Subscribed to: %s' % channel)
        client.subscribe('channel/%s/%s/%s' % (self.user, self.thing, channel))

    def pub(self, channel, msg):
        print(('Publish \'' + str(msg) + '\' to: ' + str(channel)))
        client.publish('channel/%s/%s/%s' % (self.user, self.thing, channel), msg)

    def loop(self, loopFunction):
        client.loop_start()
        while(1):
            loopFunction()

class Mqtt():

    def __init__(self, user, key, thing):
        self.user = user
        self.key = key
        self.thing = thing

    def connect(self):

        if hasattr(self, 'onConnectedCB'):
            client.on_connect = self.onConnect

        if hasattr(self, 'onDisconnectedCB'):
            client.on_disconnect = self.onDisconnectedCB

        if hasattr(self, 'onPublishedCB'):
            client.on_publish = self.onPublishedCB

        if hasattr(self, 'onDataCB'):
            client.on_message = self.on_message

        client.username_pw_set(self.user, self.key)
        client.connect('service.anto.io', 1883, 60)
        #print('Connected!')

    def onConnect(self, client, userdata, flags, rc):
        self.onConnectedCB()

    def onConnected(self, callback):
        self.onConnectedCB = callback

    def onDisconnected(self, callback):
        self.onDisconnectedCB = callback

    def onData(self, callback):
        self.onDataCB = callback

    def on_message(self, mosq, obj, msg):
        topic = msg.topic.split('/')[3]
        # send topic and msg to callback
        self.onDataCB(topic, msg.payload)

    def onPublished(self, callback):
        self.onPublishedCB = callback
