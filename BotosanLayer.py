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
    def on_message_received(self, message_protocol_entity):
        # Ack immediately then take a while to respond
        """
        Handles ever message received, if we want to take action on a message we send the message to the lower
        layers using self.toLower(MessageProtocolEntitity)
        :param message_protocol_entity: A Message of Parent class: MessageProtocolEntity
        """
        self.toLower(message_protocol_entity.ack())
        self.toLower(message_protocol_entity.ack(True))

        if DateHelper.determine_if_botosan_should_respond(message_protocol_entity.getTimestamp()):
            self.sleep_botosan()

            if message_protocol_entity.getType() == 'text':
                if message_protocol_entity.isGroupMessage():
                    self.on_group_message(message_protocol_entity)
                else:
                    self.on_text_message(message_protocol_entity)
            elif message_protocol_entity.getType() == 'media':
                self.on_media_message(message_protocol_entity)

            if message_protocol_entity.getType() == 'text' and \
                    self.regex.message_matches_a_pattern(message_protocol_entity):
                message_to_send = self.regex.generate_message_protocol_for_pattern(message_protocol_entity)
                if message_to_send is not None:
                    self.logger.info("Sending message %s", message_to_send.getBody())
                    self.simulate_botosan_preparing_answer(message_protocol_entity, message_to_send=message_to_send)
                else:
                    self.logger.info("No pattern match.")

    @ProtocolEntityCallback("receipt")
    def on_receipt(self, entity):
        self.toLower(entity.ack())

    def set_botosan_presence(self):
        self.toLower(PresenceProtocolEntity(name="Botosan"))

    def set_botosan_online(self):
        self.toLower(AvailablePresenceProtocolEntity())

    def set_botosan_disconnected(self):
        self.toLower(UnavailablePresenceProtocolEntity())

    def set_botosan_typing(self, message):
        self.toLower(OutgoingChatstateProtocolEntity(
            OutgoingChatstateProtocolEntity.STATE_TYPING,
            message.getFrom()
        ))

    def stop_botosan_typing(self, message):
        self.toLower(OutgoingChatstateProtocolEntity(
            OutgoingChatstateProtocolEntity.STATE_PAUSED,
            message.getFrom()
        ))

    def simulate_botosan_preparing_answer(self, message_protocol, message_to_send):
        self.set_botosan_presence()

        self.set_botosan_online()
        self.sleep_botosan()

        self.set_botosan_typing(message_protocol)
        self.sleep_botosan(min_time=2.0, max_time=4.0)

        self.stop_botosan_typing(message_protocol)
        self.sleep_botosan()

        self.toLower(message_to_send)

    @staticmethod
    def sleep_botosan(min_time=0.2, max_time=0.6):
        """
        Sleeps botosan for a random amount of time between min and max, defaults to 0.2 and 0.6 if none are provided.
        :param min_time: Minimum amount of time to sleep
        :param max_time: Maximum amount of time to sleep
        """
        time.sleep(random.uniform(min_time, max_time))

    def on_text_message(self, message_protocol_entity):
        """Log the body and phone from which it originated"""
        self.logger.info("Echoing %s to %s" % (message_protocol_entity.getBody(), message_protocol_entity.getFrom(True)))

    def on_media_message(self, message_protocol_entity):
        """Log the image url and phone from which it originated"""
        if message_protocol_entity.getMediaType() == "image":
            self.logger.info("Echoing image %s to %s" % (message_protocol_entity.url, message_protocol_entity.getFrom(True)))

        elif message_protocol_entity.getMediaType() == "location":
            self.logger.info("Echoing location (%s, %s) to %s" % (
                message_protocol_entity.getLatitude(), message_protocol_entity.getLongitude(),
                message_protocol_entity.getFrom(False)))

        elif message_protocol_entity.getMediaType() == "vcard":
            self.logger.info("Echoing vcard (%s, %s) to %s" % (
                message_protocol_entity.getName(), message_protocol_entity.getCardData(),
                message_protocol_entity.getFrom(True)))

    def on_group_message(self, message):
        """Log the author, participant, user and body of the message"""
        self.logger.info("Group Message: [%s]  ===  [%s]-[%s]\t%s" % (
        message.getAuthor(), message.getParticipant(), message.getFrom(), message.getBody()))
