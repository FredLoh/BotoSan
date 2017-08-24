import logging
import threading

from yowsup.layers import YowLayer


class BotoChatLayer(YowLayer):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger("botosan.logger")

    def send(self, data):
        threading.Thread(target=self.child()).start()
        self.toLower(data)

    def receive(self, data):
        self.toUpper(data)

    def child(self):
        pass
