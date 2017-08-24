from yowsup.stacks import YowStackBuilder
from yowsup.layers.auth import AuthError
from BotosanLayer import BotosanLayer
from BotoChatLayer import BotoChatLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer


class BotoSanStack(object):
    def __init__(self, credentials, encryptionEnabled=True):
        self.stack = YowStackBuilder().pushDefaultLayers(encryptionEnabled)\
            .push(BotoChatLayer).push(BotosanLayer)\
            .build()
        self.stack.setCredentials(credentials)

    def start(self):
        self.stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))
        try:
            self.stack.loop()
        except AuthError as e:
            print("Authentication Error: %s" % e.message)
