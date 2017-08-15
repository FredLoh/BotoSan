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
	
def random_estaban(message):
    beban_list = ["Estufa ","Estonia ","Estebana ","Esteban ","Estufutria Lentes ","Beban "]
	es_list = ["es ","sera ","siempre lo fue ","sueña con ser ","aspira ser ","es una "]
	adj_list = ["popo","pipi","caca","exremento", "rata cochina","traidor","nutria","gata","zorra","gordo ","gorda ","cuatrojos ","inutil ","Tonto ","tonta ","basofia","basura","puto","puta","Pato","Patricio","Pato con Lentes","vagina","pitos","traga pitos","perro","perra de Baumann", "perra de Cantu", "perra de Echeverry", "perra de mau Garcia", "perra de Jorge", "perra de Guerra", "perra de Rana", "perra de AlFredrick", "perra de Marchand", "perra de Ricky", "perra de David",
     , "perra de Ortiz", "perra de Olaf", "perra de Peña", "perra de Memo", "perra de Eduardo", "perra de Victor", "perra de Pato", "perra de Vela"]
    return TextMessageProtocolEntity(u'༼ つ ಠ益ಠ༽つ [%d]' % random.choice(beban_list) % random.choice(es_list) % random.choice(adj_list), to=message.getFrom())