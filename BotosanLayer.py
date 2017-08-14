# coding=utf-8
import random
import time
import logging
import RegexMatcher
from DateHelper import DateHelper
from yowsup.layers.interface import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from yowsup.layers.protocol_presence.protocolentities import *
from yowsup.layers.protocol_chatstate.protocolentities import *
from yowsup.common.tools import Jid
from yowsup.layers.protocol_media.protocolentities import *


class BotosanLayer(YowInterfaceLayer):
    def __init__(self):
        super(BotosanLayer, self).__init__()
        self.regex = RegexMatcher.RegexMatcher()
        self.logger = logging.getLogger("botosan.logger")

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        # Ack immediately then take a while to respond
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))

        if DateHelper.determineIfBotosanShouldRespond(messageProtocolEntity.getTimestamp()):
            self.sleepBotosan()

            if messageProtocolEntity.getType() == 'text':
                if messageProtocolEntity.isGroupMessage():
                    self.onGroupMessage(messageProtocolEntity)
                else:
                    self.onTextMessage(messageProtocolEntity)
            elif messageProtocolEntity.getType() == 'media':
                self.onMediaMessage(messageProtocolEntity)

            if messageProtocolEntity.getType() == 'text' and self.regex.doesMatchAPattern(messageProtocolEntity):
                message_to_send = self.regex.matchPatterns(messageProtocolEntity)
                if message_to_send is not None:
                    self.simulateBotosanPreparingAnswer(messageProtocolEntity, messageToSend=message_to_send)
                else:
                    self.logger.info("No pattern match.")

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def setBotosanOnline(self):
        self.toLower(AvailablePresenceProtocolEntity())

    def setBotosanDisconnect(self):
        self.toLower(UnavailablePresenceProtocolEntity())

    def setBotosanPresence(self):
        self.toLower(PresenceProtocolEntity(name="Botosan"))

    def setBotosanTyping(self, message):
        self.toLower(OutgoingChatstateProtocolEntity(
            OutgoingChatstateProtocolEntity.STATE_TYPING,
            message.getFrom()
        ))

    def stopBotosanTyping(self, message):
        self.toLower(OutgoingChatstateProtocolEntity(
            OutgoingChatstateProtocolEntity.STATE_PAUSED,
            message.getFrom()
        ))

    def simulateBotosanPreparingAnswer(self, messageProtocol, messageToSend):
        self.setBotosanPresence()

        self.setBotosanOnline()
        self.sleepBotosan()

        self.setBotosanTyping(messageProtocol)
        self.sleepBotosan(minTime=2.0, maxTime=4.0)

        self.stopBotosanTyping(messageProtocol)
        self.sleepBotosan()

        self.toLower(messageToSend)

    @staticmethod
    def sleepBotosan(minTime=0.2, maxTime=0.6):
        """
        Sleeps botosan for a random amount of time between min and max, defaults to 0.2 and 0.6 if none are provided.
        :param minTime: Minimum amount of time to sleep
        :param maxTime: Maximum amount of time to sleep
        """
        time.sleep(random.uniform(minTime, maxTime))

    def onTextMessage(self, messageProtocolEntity):
        """Log the body and phone from which it originated"""
        self.logger.info("Echoing %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(True)))

    def onMediaMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getMediaType() == "image":
            self.logger.info("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(True)))

        elif messageProtocolEntity.getMediaType() == "location":
            self.logger.info("Echoing location (%s, %s) to %s" % (
                messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(),
                messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            self.logger.info("Echoing vcard (%s, %s) to %s" % (
                messageProtocolEntity.getName(), messageProtocolEntity.getCardData(),
                messageProtocolEntity.getFrom(True)))

    def onGroupMessage(self, message):
        self.logger.info("Group Message: [%s]  ===  [%s]-[%s]\t%s" % (
        message.getAuthor(), message.getParticipant(), message.getFrom(), message.getBody()))
