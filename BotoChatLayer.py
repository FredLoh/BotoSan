import threading

from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback


class BotoChatLayer(YowInterfaceLayer):
    def __init__(self):
        super(BotoChatLayer, self).__init__()

    @ProtocolEntityCallback("receipt")
    def on_receipt(self, entity):
        self.toLower(entity.ack())

    @ProtocolEntityCallback("message")
    def on_message_received(self, message_protocol_entity):
        threading.Thread(target=self.child()).start()
        self.toLower(message_protocol_entity.ack())
        self.toLower(message_protocol_entity.ack(True))
        self.toLower(message_protocol_entity)

    def child(self):
        print('\nA new child')
