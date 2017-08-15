# coding=utf-8
import random
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity


def random_roll(message):
    """
    Rolls a number between 1 and 10.
    :param message: A message of parent class MessageProtocol
    :return: A TextMessageProtocol with the response
    """
    value = random.randint(1, 10)
    if value == 10:
        return TextMessageProtocolEntity(u'༼ つ ಠ益ಠ༽つ [%d]' % value, to=message.getFrom())
    else:
        return TextMessageProtocolEntity(u'༼ つ ◕_◕ ༽つ [%d]' % value, to=message.getFrom())

def random_raza(message):
    raza_list = ["Baumann", "Cantu", "Echeverry", "Garcia", "Jorge", "Guerra", "Lamadrid", "Fred", "Marchand", "Ricky", "David",
     "Esteban", "Ortiz", "Olaf", "Peña", "Memo", "Eduardo", "Victor", "Pato", "Vela"]
    return TextMessageProtocolEntity(random.choice(raza_list), to=message.getFrom())