# coding=utf-8
import random
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity


def randomRoll(message):
    return TextMessageProtocolEntity(u'༼ つ ◕_◕ ༽つ [%d]' % random.randint(1, 10), to=message.getFrom())