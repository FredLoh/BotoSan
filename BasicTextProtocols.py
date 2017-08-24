# coding=utf-8
import random

from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity

from JSONHandler import JSONHandler


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
    raza_list = JSONHandler.get_response_for("raza_list")
    return TextMessageProtocolEntity(random.choice(raza_list), to=message.getFrom())


def generate_insult_string():
    beban_list = JSONHandler.get_response_for("beban_list")
    es_list = JSONHandler.get_response_for("es_list")
    adj_list = JSONHandler.get_response_for("adj_list")
    insult_sentence = u'つ ಠ益ಠ༽つ ' + random.choice(beban_list) + random.choice(es_list) + random.choice(adj_list)
    return insult_sentence


def random_estaban(message):
    return TextMessageProtocolEntity(generate_insult_string(), to=message.getFrom())


def generate_eightball(message):
    response_list = JSONHandler.get_response_for("eightball_list")
    return TextMessageProtocolEntity(random.choice(response_list), to=message.getFrom())


def generate_jorgita_message(message):
    response_list = JSONHandler.get_response_for("jorge_list")
    return TextMessageProtocolEntity(random.choice(response_list), to=message.getFrom())


def generate_pato_message(message):
    pato_response_list = JSONHandler.get_response_for("pato_list")
    return TextMessageProtocolEntity(random.choice(pato_response_list), to=message.getFrom())
